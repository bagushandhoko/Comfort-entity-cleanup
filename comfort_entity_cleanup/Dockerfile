ARG BUILD_FROM=ghcr.io/home-assistant/aarch64-base:latest
FROM ${BUILD_FROM}

RUN apk add --no-cache python3 py3-pip
RUN pip install --break-system-packages requests

WORKDIR /app
COPY . /app

RUN chmod +x run.sh cleanup.py

CMD [ "/app/run.sh" ]
