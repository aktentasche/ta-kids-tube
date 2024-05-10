    path(
        "playlist/",
        views.PlaylistApiListView.as_view(),
        name="api-playlist-list",
    ),
    path(
        "playlist/<slug:playlist_id>/",
        views.PlaylistApiView.as_view(),
        name="api-playlist",
    ),
    path(
        "playlist/<slug:playlist_id>/video/",
        views.PlaylistApiVideoView.as_view(),
        name="api-playlist-video",
    ),

class ApiBaseView(APIView):
    """base view to inherit from"""

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    search_base = ""
    data = ""

    def __init__(self):
        super().__init__()
        self.response = {
            "data": False,
            "config": {
                "enable_cast": EnvironmentSettings.ENABLE_CAST,
                "downloads": AppConfig().config["downloads"],
            },
        }
        self.data = {"query": {"match_all": {}}}
        self.status_code = False
        self.context = False
        self.pagination_handler = False

    def get_document(self, document_id):
        """get single document from es"""
        path = f"{self.search_base}{document_id}"
        response, status_code = ElasticWrap(path).get()
        try:
            self.response["data"] = SearchProcess(response).process()
        except KeyError:
            print(f"item not found: {document_id}")
            self.response["data"] = False
        self.status_code = status_code

    def initiate_pagination(self, request):
        """set initial pagination values"""
        self.pagination_handler = Pagination(request)
        self.data.update(
            {
                "size": self.pagination_handler.pagination["page_size"],
                "from": self.pagination_handler.pagination["page_from"],
            }
        )

    def get_document_list(self, request, pagination=True):
        """get a list of results"""
        if pagination:
            self.initiate_pagination(request)

        es_handler = ElasticWrap(self.search_base)
        response, status_code = es_handler.get(data=self.data)
        self.response["data"] = SearchProcess(response).process()
        if self.response["data"]:
            self.status_code = status_code
        else:
            self.status_code = 404

        if pagination:
            self.pagination_handler.validate(
                response["hits"]["total"]["value"]
            )
            self.response["paginate"] = self.pagination_handler.pagination


class PlaylistApiListView(ApiBaseView):
    """resolves to /api/playlist/
    GET: returns list of indexed playlists
    """

    search_base = "ta_playlist/_search/"
    permission_classes = [AdminWriteOnly]
    valid_playlist_type = ["regular", "custom"]

    def get(self, request):
        """handle get request"""
        playlist_type = request.GET.get("playlist_type", None)
        query = {"sort": [{"playlist_name.keyword": {"order": "asc"}}]}
        if playlist_type is not None:
            if playlist_type not in self.valid_playlist_type:
                message = f"invalid playlist_type {playlist_type}"
                return Response({"message": message}, status=400)

            query.update(
                {
                    "query": {
                        "term": {"playlist_type": {"value": playlist_type}}
                    },
                }
            )

        self.data.update(query)
        self.get_document_list(request)
        return Response(self.response)

    def post(self, request):
        """subscribe/unsubscribe to list of playlists"""
        data = request.data
        try:
            to_add = data["data"]
        except KeyError:
            message = "missing expected data key"
            print(message)
            return Response({"message": message}, status=400)

        pending = []
        for playlist_item in to_add:
            playlist_id = playlist_item["playlist_id"]
            if playlist_item["playlist_subscribed"]:
                pending.append(playlist_id)
            else:
                self._unsubscribe(playlist_id)

        if pending:
            url_str = " ".join(pending)
            subscribe_to.delay(url_str, expected_type="playlist")

        return Response(data)

    @staticmethod
    def _unsubscribe(playlist_id: str):
        """unsubscribe"""
        print(f"[{playlist_id}] unsubscribe from playlist")
        PlaylistSubscription().change_subscribe(
            playlist_id, subscribe_status=False
        )


class PlaylistApiView(ApiBaseView):
    """resolves to /api/playlist/<playlist_id>/
    GET: returns metadata dict of playlist
    """

    search_base = "ta_playlist/_doc/"
    permission_classes = [AdminWriteOnly]
    valid_custom_actions = ["create", "remove", "up", "down", "top", "bottom"]

    def get(self, request, playlist_id):
        # pylint: disable=unused-argument
        """get request"""
        self.get_document(playlist_id)
        return Response(self.response, status=self.status_code)

    def post(self, request, playlist_id):
        """post to custom playlist to add a video to list"""
        playlist = YoutubePlaylist(playlist_id)
        if not playlist.is_custom_playlist():
            message = f"playlist with ID {playlist_id} is not custom"
            return Response({"message": message}, status=400)

        action = request.data.get("action")
        if action not in self.valid_custom_actions:
            message = f"invalid action: {action}"
            return Response({"message": message}, status=400)

        video_id = request.data.get("video_id")
        if action == "create":
            playlist.add_video_to_playlist(video_id)
        else:
            hide = UserConfig(request.user.id).get_value("hide_watched")
            playlist.move_video(video_id, action, hide_watched=hide)

        return Response({"success": True}, status=status.HTTP_201_CREATED)

    def delete(self, request, playlist_id):
        """delete playlist"""
        print(f"{playlist_id}: delete playlist")
        delete_videos = request.GET.get("delete-videos", False)
        if delete_videos:
            YoutubePlaylist(playlist_id).delete_videos_playlist()
        else:
            YoutubePlaylist(playlist_id).delete_metadata()

        return Response({"success": True})


class PlaylistApiVideoView(ApiBaseView):
    """resolves to /api/playlist/<playlist_id>/video
    GET: returns list of videos in playlist
    """

    search_base = "ta_video/_search/"

    def get(self, request, playlist_id):
        """handle get request"""
        self.data["query"] = {
            "term": {"playlist.keyword": {"value": playlist_id}}
        }
        self.data.update({"sort": [{"published": {"order": "desc"}}]})

        self.get_document_list(request)
        return Response(self.response, status=self.status_code)