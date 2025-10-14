#!/usr/bin/with-contenv bashio
bashio::log.info "Starting Comfort Entity Cleanup..."

# Jalankan Python script utama
python3 /app/cleanup.py

bashio::log.info "Comfort Entity Cleanup finished."
