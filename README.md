# ta-kids-tube

ta-kids-tube is a video platform designed for kids and their parents. It uses [TubeArchivist](https://github.com/tubearchivist/tubearchivist) as backend for video storage and retrieval.

## Motivation

[TubeArchivist](https://github.com/tubearchivist/tubearchivist) is a great solution to making YouTube videos available offline using a hassle-free web interface. It also has some very nice features for searching, indexing and subscribing to channels. 

My use case however is very specific and currently not entirely covered by TubeArchivist: A browser based video platform for my kids. They love watching all kinds of videos on YouTube, but I as a parent always have to be present to select new videos based on what my kids are screaming for. Also, YouTube might not work while on the road, so I also needed a way to play videos offline.

## Features

- Countdown timer to stop the video playback (after all, kids should not watch that much TV)
- Autoplay of the next video in the playlist (see also [tubearchivist#226](https://github.com/tubearchivist/tubearchivist/issues/226))
- Bulk editing of playlist (for example for downloading a bunch of Peppa Pig Videos using the [browser extension](https://github.com/tubearchivist/browser-extension) and then bulk add them to a Peppa Pig playlist)

## Limitations

- This is supposed to be an addition to the TubeArchivist functionality, so downloading, subscribing etc. have to be done in the TubeArchivist frontend

## Why not contribute to TubeArchivist?

Even though I am a python guy I have never worked with Django. I took a look at the TubeArchivist codebase and was quickly overwhelmed by the complexity and understanding Django and the codebase would take time that I do not have as a busy parent ;) 

So I intuitively drifted towards the frontend technology that I know: Vue.js. Furthermore some of my wanted features are likely impossible to implement using Django (e.g. remote control).

# Tech stack

- [Vue.js](https://github.com/vuejs/core) with [vuetify](https://github.com/vuetifyjs/vuetify) and [pinia](https://github.com/vuejs/pinia) for the frontend
- A manually (with chatGPT, duh) created openapi.yaml based on the [TA API](https://docs.tubearchivist.com/api/introduction/)
- [openapi-typescript-codegen](https://github.com/ferdikoomen/openapi-typescript-codegen) to generate Typescript code from the TubeArchivist [OpenAPI](https://swagger.io/specification/) definition to be used in the Vue.js frontend
- docker compose to run everything
- VSCode devcontainers for development


# OpenAPI definition
[ta_openapi.yaml](ta_openapi.yaml) contains a subset of the TA API in the openapi format. It is manually maintained and might break for future version of TA. The version of the OpenAPI definition follows the TA release versions.

## Debug with swagger UI

Prerequisites: Linux with docker installed

1. Replace IP of your main TA instance in [ta_openapi.yaml](ta_openapi.yaml) (under servers)
2. Add "- DISABLE_CORS=True" to the main TA docker-compose.yaml for the tubearchivist container (note the security implications)
3. docker compose down-up TA
4. Start the swagger-ui by running ./run_swagger_ui.sh
5. Click "Authorize" and insert "Token abcdedf" with abcdedf being your auth token retrieved from the TA UI


# Development
Get VScode with dev containers extension then re-open this repo as dev container. 
Run the task "npm run dev" to start the Vue dev server.


# Deploy

TBD
