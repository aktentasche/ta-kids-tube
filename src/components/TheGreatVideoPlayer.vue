<template>
  <v-container>
    TheGreatVideoPlayer
    <video-player :src="video_src_url" :poster="video_poster_url" controls />
  </v-container>
</template>

<script setup lang="ts">
import { VideoPlayer } from "@videojs-player/vue";
import "video.js/dist/video-js.css";

// import { VideoService } from "@/ta_openapi";
import { VideoService } from "@/ta_openapi/services/VideoService";

import { ref, onMounted } from "vue";

const props = defineProps<{
  ta_youtube_id: string;
}>();

onMounted(() => {
  VideoService.getVideo(props.ta_youtube_id).then((r) =>
    console.log(import.meta.env.VITE_TA_BASE_URL + r.data.media_url),
  );
});

const video_src_url = ref("");
const video_poster_url = ref("");

console.log(props.ta_youtube_id);
</script>
