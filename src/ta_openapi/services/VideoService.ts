/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { Pagination } from '../models/Pagination';
import type { Video } from '../models/Video';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class VideoService {
    /**
     * Retrieve a list of videos
     * @returns any A list of videos successfully retrieved.
     * @throws ApiError
     */
    public static listVideos(): CancelablePromise<{
        data?: Array<Video>;
        paginate?: Pagination;
    }> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/video/',
            errors: {
                404: `No videos found.`,
            },
        });
    }
    /**
     * Retrieve metadata for a single video
     * @param videoId
     * @returns Video Video metadata retrieved successfully.
     * @throws ApiError
     */
    public static getVideo(
        videoId: string,
    ): CancelablePromise<Video> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/video/{video_id}/',
            path: {
                'video_id': videoId,
            },
            errors: {
                404: `Video not found.`,
            },
        });
    }
    /**
     * Delete a single video
     * @param videoId
     * @returns any Video deleted successfully.
     * @throws ApiError
     */
    public static deleteVideo(
        videoId: string,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/video/{video_id}/',
            path: {
                'video_id': videoId,
            },
            errors: {
                404: `Video not found.`,
            },
        });
    }
}
