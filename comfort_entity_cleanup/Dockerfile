ARG BUILD_FROM=ghcr.io/hassio-addons/base:13.2.2
FROM ${BUILD_FROM}

# Install Python dan pip
RUN apk add --no-cache python3 py3-pip

# Copy semua file ke container
COPY . /app
WORKDIR /app

# Install dependencies jika ada
RUN pip install --no-cache-dir -r requirements.txt || true

# Jalankan script utama
CMD ["python3", "/app/run.py"]
