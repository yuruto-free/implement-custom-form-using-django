ARG ARCHITECTURE=arm64v8

From ${ARCHITECTURE}/postgres:17-alpine3.21
ARG TZ=Asia/Tokyo

LABEL maintainer="yuruto-free"
LABEL description="Build the environment of PostgreSQL"

RUN    apk update \
    && apk upgrade \
    && apk add --no-cache bash tzdata \
    && ln -s /usr/share/zoneinfo/${TZ} /etc/localtime