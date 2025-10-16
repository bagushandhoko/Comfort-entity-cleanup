# Base image resmi Home Assistant
ARG BUILD_FROM=ghcr.io/hassio-addons/base:15.0.6
FROM ${BUILD_FROM}

# Install dependensi Python
RUN apk add --no-cache python3 py3-pip

# Set folder kerja
WORKDIR /app
COPY . /app

# Izin eksekusi
RUN chmod +x /app/run.sh
RUN chmod +x /app/run.py

# Install library Python
RUN pip install --no-cache-dir -r requirements.txt || true

# Jalankan script utama
CMD [ "/app/run.sh" ]
