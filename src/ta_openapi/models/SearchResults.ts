/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { SearchResultChannel } from './SearchResultChannel';
import type { SearchResultFulltext } from './SearchResultFulltext';
import type { SearchResultPlaylist } from './SearchResultPlaylist';
import type { SearchResultVideo } from './SearchResultVideo';
export type SearchResults = {
    /**
     * The search results grouped by type
     */
    results?: {
        video_results?: Array<SearchResultVideo>;
        channel_results?: Array<SearchResultChannel>;
        playlist_results?: Array<SearchResultPlaylist>;
        fulltext_results?: Array<SearchResultFulltext>;
    };
    /**
     * The type of query performed
     */
    queryType?: string;
};

