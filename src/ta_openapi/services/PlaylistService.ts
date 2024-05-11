/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { Pagination } from '../models/Pagination';
import type { Playlist } from '../models/Playlist';
import type { PlaylistModification } from '../models/PlaylistModification';
import type { PlaylistSubscriptionUpdate } from '../models/PlaylistSubscriptionUpdate';
import type { Video } from '../models/Video';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class PlaylistService {
    /**
     * Retrieve a list of all playlists
     * @param playlistType Filter playlists by type (regular or custom)
     * @returns any A list of playlists retrieved successfully.
     * @throws ApiError
     */
    public static listPlaylists(
        playlistType?: string,
    ): CancelablePromise<{
        data?: Array<Playlist>;
        paginate?: Pagination;
    }> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/playlist/',
            query: {
                'playlist_type': playlistType,
            },
            errors: {
                400: `Invalid playlist type provided.`,
                404: `No playlists found.`,
            },
        });
    }
    /**
     * Subscribe or unsubscribe from a list of playlists
     * @param requestBody
     * @returns any Playlist subscription status updated.
     * @throws ApiError
     */
    public static updatePlaylistSubscriptions(
        requestBody: PlaylistSubscriptionUpdate,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/playlist/',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                400: `Missing or invalid request body.`,
            },
        });
    }
    /**
     * Retrieve metadata for a specific playlist
     * @param playlistId
     * @returns Playlist Playlist metadata retrieved successfully.
     * @throws ApiError
     */
    public static getPlaylist(
        playlistId: string,
    ): CancelablePromise<Playlist> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/playlist/{playlist_id}/',
            path: {
                'playlist_id': playlistId,
            },
            errors: {
                404: `Playlist not found.`,
            },
        });
    }
    /**
     * Modify a playlist (e.g., add or move videos)
     * @param playlistId
     * @param requestBody
     * @returns any Playlist modified successfully.
     * @throws ApiError
     */
    public static modifyPlaylist(
        playlistId: string,
        requestBody: PlaylistModification,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/playlist/{playlist_id}/',
            path: {
                'playlist_id': playlistId,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                400: `Invalid action or request body.`,
            },
        });
    }
    /**
     * Delete a specific playlist
     * @param playlistId
     * @returns any Playlist deleted successfully.
     * @throws ApiError
     */
    public static deletePlaylist(
        playlistId: string,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/playlist/{playlist_id}/',
            path: {
                'playlist_id': playlistId,
            },
        });
    }
    /**
     * Retrieve all videos within a specific playlist
     * @param playlistId
     * @returns Video List of videos retrieved successfully.
     * @throws ApiError
     */
    public static listPlaylistVideos(
        playlistId: string,
    ): CancelablePromise<Array<Video>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/playlist/{playlist_id}/video/',
            path: {
                'playlist_id': playlistId,
            },
        });
    }
}
