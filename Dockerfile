ARG BUILD_FROM=ghcr.io/hassio-addons/base:13.2.2
FROM ${BUILD_FROM}

RUN apk add --no-cache python3 py3-pip

COPY . /app
WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt || true

CMD ["python3", "/app/run.py"]
