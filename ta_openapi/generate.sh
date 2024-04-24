#!/bin/bash
#!/bin/bash
VERSION="v0.4.7"

# echo "Cloning TubeArchivist $VERSION"
# git clone https://github.com/tubearchivist/tubearchivist.git
# cd tubearchivist
# git checkout $VERSION
# cd ..

echo "Adding drf-spectacular to TA requirements.txt"
echo "drf-spectacular==0.27.2" >> ./tubearchivist/tubearchivist/requirements.txt

echo "Set TA_HOST to localhost in TA docker-compose.yml"
sed -i 's|- TA_HOST=tubearchivist.local         # set your host name|- TA_HOST=localhost         # set your host name|' ./tubearchivist/docker-compose.yml

echo "Use TA Dockerfile instead of image from Dockerhub un TA docker-compose.yml"
sed -i 's|image: bbilly1/tubearchivist|build: .|' ./tubearchivist/docker-compose.yml

echo "add drf-spectacular to TA settings.py INSTALLED_APPS"
sed -i '/INSTALLED_APPS = \[/,/^]$/ {/^]$/i\    "drf_spectacular"
}' /home/jonas/git/ta-kids-tube/ta_openapi/tubearchivist/tubearchivist/config/settings.py

# TBD remove tubearchivist folder