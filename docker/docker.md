# Docker Cheat Sheet

## Info
**docker version**
Displays Docker version

**docker info**
Displays system information

**docker stats**
Displays live containers resource usage

**docker ps**
List locally stored images.

**docker images**
List images

**docker history _imagename_**
Shows the history of an image

**docker logs _containername_**
Fetch the logs of a container


## Build
**docker build _imagename_** .
Builds an image from a Dockerfile in the current directory

**docker build -t '_imagename_'** .
Builds and tags image with a name

**docker image rm _imagename:4.7_**
Deletes an image locally


## Run
**docker container run _containername_**
Runs container

**docker container run -d _containername_**
Runs container detached

**docker start _containername_ _anothercontainer_**
Start one or more stopped containers

**docker stop _containername_**
Stops a running container

**docker kill _containername_**
Kills a running container


## Remote
**docker pull _imagename:2.4_**
Pulls an image from [Docker Hub](https://hub.docker.com/)

**docker push _reponame/imagename:1.0_**
Push image or repository to [Docker Hub](https://hub.docker.com/)

