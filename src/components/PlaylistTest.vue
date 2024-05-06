<template>
  asd
  <v-container>asd </v-container>
</template>

<script lang="ts" setup>
import { ref } from "vue";

import { PlaylistService } from "@/ta_openapi";

await PlaylistService.listPlaylists().then((r) => console.log(r));
</script>
