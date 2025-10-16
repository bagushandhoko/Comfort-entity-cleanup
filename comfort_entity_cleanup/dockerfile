ARG BUILD_FROM=ghcr.io/hassio-addons/base:15.0.6
FROM ${BUILD_FROM}

# Install Python
RUN apk add --no-cache python3 py3-pip

# Working directory
WORKDIR /app

# Copy addon files
COPY . /app

# Permissions
RUN chmod +x /app/run.sh /app/cleanup.py

# Install dependencies (if any)
RUN pip install --no-cache-dir -r /app/requirements.txt || true

# Default command
CMD [ "/app/run.sh" ]
