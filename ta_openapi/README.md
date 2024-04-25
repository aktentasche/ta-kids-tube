This folder contains a subset of the TA API in the openapi format. It is manually maintained and might break for future version of TA. The version of the OpenAPI definition follows the TA release versions.

# Debug with swagger UI

Prerequisites: Linux with docker installed

1. Replace IP of your main TA instance in openapi.yaml (under servers)
2. Add "- DISABLE_CORS=True" to the main TA docker-compose.yaml for the tubearchivist container (note the security implications)
3. down-up TA
4. Start the swagger-ui by running ./run_swagger_ui.sh
5. Click "Authorize" and insert "Token abcdedf" with abcdedf being your auth token retrieved from the TA UI