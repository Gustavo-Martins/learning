# Docker Cheat Sheet

## Info
**docker ps**
List locally stored images.


## Build
**docker build _imagename_**
Build an image from a Dockerfile in the current directory

**docker image rm _imagename:4.7_**
Deletes an image locally


## Run
**docker container run _containername_**
Runs container

**docker container run -d _containername_**
Runs container detached


## Remote
**docker pull _imagename:2.4_**
Pulls an image from [Docker Hub](https://hub.docker.com/)

**docker push _reponame/imagename:1.0_**
Push image to [Docker Hub](https://hub.docker.com/)

