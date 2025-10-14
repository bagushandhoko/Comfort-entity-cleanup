ARG BUILD_FROM=ghcr.io/hassio-addons/base:15.0.6
FROM ${BUILD_FROM}

# Pastikan Python3 dan pip terinstall
RUN apk add --no-cache python3 py3-pip

# Set working directory
WORKDIR /app

# Copy seluruh file addon ke dalam container
COPY . /app

# Permission agar script bisa dijalankan
RUN chmod +x /app/run.sh

# Pastikan script cleanup.py dapat dijalankan manual juga
RUN chmod +x /app/cleanup.py

# Entry point: Home Assistant akan menjalankan ini
CMD [ "/app/run.sh" ]
