#!/usr/bin/env python3
import os
import requests
import logging
import sys

# -----------------------------
# Setup logging
# -----------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)

# -----------------------------
# Home Assistant Config
# -----------------------------
HA_URL = os.environ.get("HA_URL", "http://homeassistant.local:8123")
HA_TOKEN = os.environ.get("HA_TOKEN", "YOUR_LONG_LIVED_ACCESS_TOKEN")

HEADERS = {
    "Authorization": f"Bearer {HA_TOKEN}",
    "Content-Type": "application/json",
}

# -----------------------------
# Helper functions
# -----------------------------
def get_entities():
    """Ambil semua entitas dari HA"""
    try:
        r = requests.get(f"{HA_URL}/api/states", headers=HEADERS, timeout=10)
        r.raise_for_status()
        return r.json()
    except requests.RequestException as e:
        logger.error(f"Gagal mengambil entitas: {e}")
        return []

def delete_entity(entity_id):
    """Hapus entitas via Home Assistant API"""
    try:
        r = requests.delete(f"{HA_URL}/api/states/{entity_id}", headers=HEADERS, timeout=10)
        if r.status_code == 200:
            logger.info(f"Deleted entity: {entity_id}")
        else:
            logger.warning(f"Failed to delete {entity_id}, status: {r.status_code}")
    except requests.RequestException as e:
        logger.error(f"Error deleting {entity_id}: {e}")

# -----------------------------
# Main cleanup logic
# -----------------------------
def main():
    logger.info("Starting Comfort Entity Cleanup...")

    entities = get_entities()
    if not entities:
        logger.warning("Tidak ada entitas ditemukan. Hentikan proses.")
        return

    for entity in entities:
        if entity.get("state") == "unavailable":
            entity_id = entity["entity_id"]
            logger.info(f"Found unavailable entity: {entity_id}")
            delete_entity(entity_id)

    logger.info("Cleanup selesai!")

if __name__ == "__main__":
    main()
