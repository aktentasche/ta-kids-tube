# ta-kids-tube

ta-kids-tube is a video platform designed for kids and their parents. It uses [TubeArchivist](https://github.com/tubearchivist/tubearchivist) as backend for video storage and retrieval.




## Motivation

[TubeArchivist](https://github.com/tubearchivist/tubearchivist) is a great solution to making YouTube videos available offline using a hassle-free web interface. It also has some very nice features for searching, indexing and subscribing to channels. 

My use case however is very specific and currently not entirely covered by TubeArchivist: A browser based video platform for my kids. They love watching all kinds of videos on YouTube, but I as a parent always have to be present to select new videos based on what my kids are screaming for. Also, YouTube might not work while on the road, so I also needed a way to play videos offline.

## Features

- Countdown timer to stop the video playback (after all, kids should not watch that much TV)
- Autoplay of the next video in the playlist (see also [tubearchivist#226](https://github.com/tubearchivist/tubearchivist/issues/226))
- Bulk editing of playlist (for example for downloading a bunch of Peppa Pig Videos using the [browser extension](https://github.com/tubearchivist/browser-extension) and then bulk add them to a Peppa Pig playlist)
- Remote playback control via browser on different machine than where the video is played

## Limitations

- This is supposed to be an addition to the TubeArchivist functionality, so downloading, subscribing etc. have to be done in the TubeArchivist frontend
- Currently only one concurrent playback is supported w.r.t. remote control

## Why not contribute to TubeArchivist?

Even though I am a python guy I have never worked with Django. I took a look at the TubeArchivist codebase and was quickly overwhelmed by the complexity and understanding Django and the codebase would take time that I do not have as a busy parent ;) 

So I intuitively drifted towards the frontend technology that I know: Vue.js. Furthermore some of my wanted features are likely impossible to implement using Django (e.g. remote control).


## Tech stack

- Vue.js with pinia for the frontend
- [drf-yasg](https://github.com/axnsan12/drf-yasg) to obtain an [OpenAPI](https://swagger.io/specification/) definition of the TubeArchivist API
- [https://github.com/ferdikoomen/openapi-typescript-codegen](openapi-typescript-codegen) to generate Typescript code from the TubeArchivist OpenAPI definition to be used in the Vue.js frontend
- MQTT broker middleware for remote function calls
- docker compose to run everything