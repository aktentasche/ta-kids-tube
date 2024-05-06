/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class PlaylistService {
    /**
     * Returns list of indexed playlists
     * @param playlistType Type of playlist to filter by.
     * @returns any Successfully retrieved list of playlists.
     * @throws ApiError
     */
    public static listPlaylists(
        playlistType?: 'regular' | 'custom',
    ): CancelablePromise<{
        data?: Array<{
            playlist_id?: string;
            playlist_name?: string;
            playlist_description?: boolean;
            playlist_active?: boolean;
            playlist_channel?: string;
            playlist_channel_id?: string;
            playlist_subscribed?: boolean;
            playlist_thumbnail?: string;
            playlist_last_refresh?: string;
            playlist_type?: string;
            playlist_entries?: Array<{
                youtube_id?: string;
                title?: string;
                uploader?: string;
                idx?: number;
                downloaded?: boolean;
            }>;
            _index?: string;
            _score?: number;
        }>;
        config?: {
            enable_cast?: boolean;
            downloads?: {
                limit_speed?: boolean;
                sleep_interval?: number;
                autodelete_days?: boolean;
                format?: string;
                format_sort?: boolean;
                add_metadata?: boolean;
                add_thumbnail?: boolean;
                subtitle?: boolean;
                subtitle_source?: boolean;
                subtitle_index?: boolean;
                comment_max?: boolean;
                comment_sort?: string;
                cookie_import?: boolean;
                throttledratelimit?: boolean;
                extractor_lang?: boolean;
                integrate_ryd?: boolean;
                integrate_sponsorblock?: boolean;
            };
        };
        paginate?: {
            page_size?: number;
            page_from?: number;
            prev_pages?: boolean;
            current_page?: number;
            max_hits?: boolean;
            params?: string;
            last_page?: boolean;
            next_pages?: Array<string>;
            total_hits?: number;
        };
    }> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/api/playlist/',
            query: {
                'playlist_type': playlistType,
            },
            errors: {
                400: `Bad request due to invalid parameters.`,
            },
        });
    }
}
