# ==========================================
# Comfort Entity Cleanup - Dockerfile Final
# Raspberry Pi 3B+ / ARMv7
# ==========================================

# Gunakan base image Python resmi HA
ARG BUILD_FROM=ghcr.io/hassio-addons/base-python:13.2.2
FROM ${BUILD_FROM}

# Install Python 3 dan pip (untuk jaga-jaga)
RUN apk add --no-cache python3 py3-pip

# Copy semua file add-on dari repo ke /app
COPY . /app

# Set working directory
WORKDIR /app

# Pastikan semua script Python executable (optional)
RUN chmod +x /app/run.py

# Jalankan script utama saat container start
CMD ["python3", "/app/run.py"]
