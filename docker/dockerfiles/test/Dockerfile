FROM ubuntu

RUN apt-get update \
  && DEBIAN_FRONTEND=noninteractive apt-get install -yq \
  python3-pip

ENTRYPOINT ["dumb-init"]
