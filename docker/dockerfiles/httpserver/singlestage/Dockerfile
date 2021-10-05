FROM ubuntu

RUN apt-get update \
  && DEBIAN_FRONTEND=noninteractive apt-get install -yq \
  automake \
  build-essential \
  dumb-init \
  libmicrohttpd-dev \
  libtool \
  wget

ARG HTTPSERVER_VERSION=0.18.2
COPY ${HTTPSERVER_VERSION}.tar.gz .

RUN tar xf ${HTTPSERVER_VERSION}.tar.gz \
  && cd libhttpserver-${HTTPSERVER_VERSION} \
  && ./bootstrap \
  && mkdir build \
  && cd build \
  && ../configure \
  && make -j4 \
  && make install

COPY server.cpp .

RUN g++ -L/usr/local/lib server.cpp -o server -lhttpserver

ENV LD_LIBRARY_PATH=/usr/local/lib
ENTRYPOINT ["dumb-init"]
CMD ["/server"]
