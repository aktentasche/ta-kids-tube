<template>
  <v-container>
    TheGreatVideoPlayer
    <!-- <video-player :src="video_src_url" :poster="video_poster_url" controls /> -->
    <video ref="videoPlayer" class="video-js"></video>
  </v-container>
</template>

<script setup lang="ts">
import videojs from "video.js";
import "video.js/dist/video-js.css";

import { VideoService } from "@/ta_openapi/services/VideoService";

import { ref } from "vue";

const props = defineProps<{
  ta_youtube_id: string;
}>();

VideoService.getVideo(props.ta_youtube_id).then(async (r) => {
  video_src_url.value =
    import.meta.env.VITE_TAKIDSTUBE_VIDEO_SERVER_URL + r.data?.media_url;
});

const video_src_url = ref("");
const video_poster_url = ref("");
</script>
