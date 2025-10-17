ARG BUILD_FROM=ghcr.io/hassio-addons/base:15.0.6
FROM ${BUILD_FROM}

RUN apk add --no-cache python3 py3-pip

WORKDIR /app
COPY . /app

RUN chmod +x run.sh
RUN chmod +x cleanup.py

CMD [ "/app/run.sh" ]
