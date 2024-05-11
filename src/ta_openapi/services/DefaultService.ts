/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { SearchResults } from '../models/SearchResults';
import type { WatchedRequest } from '../models/WatchedRequest';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class DefaultService {
    /**
     * Run a search with the string in the query parameter
     * @param query The search query string
     * @returns SearchResults Search results
     * @throws ApiError
     */
    public static getSearch(
        query: string,
    ): CancelablePromise<SearchResults> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/search/',
            query: {
                'query': query,
            },
            errors: {
                400: `Bad request`,
            },
        });
    }
    /**
     * Change watched state of video, channel, or playlist
     * @param requestBody
     * @returns any Success message
     * @throws ApiError
     */
    public static postWatched(
        requestBody: WatchedRequest,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/watched/',
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                400: `Bad request`,
            },
        });
    }
}
