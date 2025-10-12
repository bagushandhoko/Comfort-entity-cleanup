# Base image Home Assistant resmi ARMv7
ARG BUILD_FROM=ghcr.io/hassio-addons/base:14.3.2
FROM ${BUILD_FROM}

# Install Python 3 dan pip
RUN apk add --no-cache python3 py3-pip

# Copy semua file repo
COPY . /app
WORKDIR /app

# Jalankan script utama
CMD ["python3", "/app/run.py"]
