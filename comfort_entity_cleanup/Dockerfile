# Gunakan base image Home Assistant yang stabil
ARG BUILD_FROM=ghcr.io/hassio-addons/base:14.3.2
FROM ${BUILD_FROM}

# Install Python
RUN apk add --no-cache python3 py3-pip

# Copy semua file dari repo
COPY . /app
WORKDIR /app

# Jalankan script Python
CMD ["python3", "/app/run.py"]
