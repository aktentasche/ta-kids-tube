    path(
        "video/",
        views.VideoApiListView.as_view(),
        name="api-video-list",
    ),
    path(
        "video/<slug:video_id>/",
        views.VideoApiView.as_view(),
        name="api-video",
    ),
    path(
        "video/<slug:video_id>/progress/",
        views.VideoProgressView.as_view(),
        name="api-video-progress",
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

class VideoApiView(ApiBaseView):
    """resolves to /api/video/<video_id>/
    GET: returns metadata dict of video
    """

    search_base = "ta_video/_doc/"
    permission_classes = [AdminWriteOnly]

    def get(self, request, video_id):
        # pylint: disable=unused-argument
        """get request"""
        self.get_document(video_id)
        return Response(self.response, status=self.status_code)

    def delete(self, request, video_id):
        # pylint: disable=unused-argument
        """delete single video"""
        message = {"video": video_id}
        try:
            YoutubeVideo(video_id).delete_media_file()
            status_code = 200
            message.update({"state": "delete"})
        except FileNotFoundError:
            status_code = 404
            message.update({"state": "not found"})

        return Response(message, status=status_code)

class VideoApiListView(ApiBaseView):
    """resolves to /api/video/
    GET: returns list of videos
    """

    search_base = "ta_video/_search/"

    def get(self, request):
        """get request"""
        self.data.update({"sort": [{"published": {"order": "desc"}}]})
        self.get_document_list(request)

        return Response(self.response)

class VideoProgressView(ApiBaseView):
    """resolves to /api/video/<video_id>/progress/
    handle progress status for video
    """

    def get(self, request, video_id):
        """get progress for a single video"""
        user_id = request.user.id
        key = f"{user_id}:progress:{video_id}"
        video_progress = RedisArchivist().get_message(key)
        position = video_progress.get("position", 0)

        self.response = {
            "youtube_id": video_id,
            "user_id": user_id,
            "position": position,
        }
        return Response(self.response)

    def post(self, request, video_id):
        """set progress position in redis"""
        position = request.data.get("position", 0)
        key = f"{request.user.id}:progress:{video_id}"
        message = {"position": position, "youtube_id": video_id}
        RedisArchivist().set_message(key, message)
        self.response = request.data
        return Response(self.response)

    def delete(self, request, video_id):
        """delete progress position"""
        key = f"{request.user.id}:progress:{video_id}"
        RedisArchivist().del_message(key)
        self.response = {"progress-reset": video_id}

        return Response(self.response)


# path(
#     "video/<slug:video_id>/comment/",
#     views.VideoCommentView.as_view(),
#     name="api-video-comment",
# ),


# path(
#     "video/<slug:video_id>/similar/",
#     views.VideoSimilarView.as_view(),
#     name="api-video-similar",
# ),
# path(
#     "video/<slug:video_id>/sponsor/",
#     views.VideoSponsorView.as_view(),
#     name="api-video-sponsor",
# ),



# class VideoSimilarView(ApiBaseView):
#     """resolves to /api/video/<video-id>/similar/
#     GET: return max 6 videos similar to this
#     """

#     search_base = "ta_video/_search/"

#     def get(self, request, video_id):
#         """get similar videos"""
#         self.data = {
#             "size": 6,
#             "query": {
#                 "more_like_this": {
#                     "fields": ["tags", "title"],
#                     "like": {"_id": video_id},
#                     "min_term_freq": 1,
#                     "max_query_terms": 25,
#                 }
#             },
#         }
#         self.get_document_list(request, pagination=False)
#         return Response(self.response, status=self.status_code)


# class VideoSponsorView(ApiBaseView):
#     """resolves to /api/video/<video_id>/sponsor/
#     handle sponsor block integration
#     """

#     search_base = "ta_video/_doc/"

#     def get(self, request, video_id):
#         """get sponsor info"""
#         # pylint: disable=unused-argument

#         self.get_document(video_id)
#         if not self.response.get("data"):
#             message = {"message": "video not found"}
#             return Response(message, status=404)

#         sponsorblock = self.response["data"].get("sponsorblock")

#         return Response(sponsorblock)

#     def post(self, request, video_id):
#         """post verification and timestamps"""
#         if "segment" in request.data:
#             response, status_code = self._create_segment(request, video_id)
#         elif "vote" in request.data:
#             response, status_code = self._vote_on_segment(request)

#         return Response(response, status=status_code)

#     @staticmethod
#     def _create_segment(request, video_id):
#         """create segment in API"""
#         start_time = request.data["segment"]["startTime"]
#         end_time = request.data["segment"]["endTime"]
#         response, status_code = SponsorBlock(request.user.id).post_timestamps(
#             video_id, start_time, end_time
#         )

#         return response, status_code

#     @staticmethod
#     def _vote_on_segment(request):
#         """validate on existing segment"""
#         user_id = request.user.id
#         uuid = request.data["vote"]["uuid"]
#         vote = request.data["vote"]["yourVote"]
#         response, status_code = SponsorBlock(user_id).vote_on_segment(
#             uuid, vote
#         )

#         return response, status_code
