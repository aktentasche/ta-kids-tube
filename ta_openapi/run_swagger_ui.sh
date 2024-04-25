#!/bin/bash
docker run -p 80:8080 -e SWAGGER_JSON=/foo/openapi.yaml -v .:/foo swaggerapi/swagger-ui