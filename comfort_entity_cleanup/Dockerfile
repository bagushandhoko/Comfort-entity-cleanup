# Gunakan base image Home Assistant minimal + Python
ARG BUILD_FROM=ghcr.io/hassio-addons/base:13.2.2
FROM ${BUILD_FROM}

# Install Python3 dan pip
RUN apk add --no-cache python3 py3-pip

# Set working directory
WORKDIR /app

# Copy semua file dari repository ke /app
COPY . /app

# Install dependencies (jika ada requirements.txt)
RUN if [ -f requirements.txt ]; then pip3 install --no-cache-dir -r requirements.txt; fi

# Pastikan script bisa dieksekusi
RUN chmod +x /app/run.py

# Jalankan script utama
CMD ["python3", "/app/run.py"]
