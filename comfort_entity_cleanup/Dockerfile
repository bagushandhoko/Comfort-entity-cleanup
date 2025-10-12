# Gunakan base image dengan Python
ARG BUILD_FROM=ghcr.io/hassio-addons/base-python:13.2.2
FROM ${BUILD_FROM}

# Copy semua file dari repo
COPY . /app

# Set working directory
WORKDIR /app

# Jalankan script utama
CMD ["python3", "/app/run.py"]
