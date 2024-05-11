/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { VideoProgress } from '../models/VideoProgress';
import type { VideoProgressInput } from '../models/VideoProgressInput';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class VideoProgressService {
    /**
     * Get progress of a video for a user
     * @param videoId
     * @returns VideoProgress Video progress retrieved successfully.
     * @throws ApiError
     */
    public static getVideoProgress(
        videoId: string,
    ): CancelablePromise<VideoProgress> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/video/{video_id}/progress/',
            path: {
                'video_id': videoId,
            },
        });
    }
    /**
     * Set progress of a video
     * @param videoId
     * @param requestBody
     * @returns any Video progress updated successfully.
     * @throws ApiError
     */
    public static setVideoProgress(
        videoId: string,
        requestBody: VideoProgressInput,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/video/{video_id}/progress/',
            path: {
                'video_id': videoId,
            },
            body: requestBody,
            mediaType: 'application/json',
        });
    }
    /**
     * Reset video progress
     * @param videoId
     * @returns any Video progress reset successfully.
     * @throws ApiError
     */
    public static resetVideoProgress(
        videoId: string,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/video/{video_id}/progress/',
            path: {
                'video_id': videoId,
            },
        });
    }
}
