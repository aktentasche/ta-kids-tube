#!/bin/bash
docker run -p 80:8080 -e SWAGGER_JSON=/ta_openapi/ta_openapi.yaml -v .:/ta_openapi swaggerapi/swagger-ui