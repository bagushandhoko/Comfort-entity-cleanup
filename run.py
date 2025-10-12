import requests
import os
import time

HA_TOKEN = os.getenv("SUPERVISOR_TOKEN")
HA_URL = "http://supervisor/core/api"

HEADERS = {
    "Authorization": f"Bearer {HA_TOKEN}",
    "Content-Type": "application/json",
}

def get_entities():
    resp = requests.get(f"{HA_URL}/states", headers=HEADERS)
    resp.raise_for_status()
    return resp.json()

def delete_entity(entity_id):
    # Hapus entitas dari registry
    url = f"{HA_URL}/config/entity_registry/{entity_id}"
    r = requests.delete(url, headers=HEADERS)
    if r.status_code in (200, 202, 204):
        print(f"Deleted: {entity_id}")
    else:
        print(f"Failed to delete {entity_id}: {r.status_code}")

def cleanup():
    print("🔍 Scanning for unavailable entities...")
    entities = get_entities()
    count = 0
    for e in entities:
        if e["state"] == "unavailable":
            delete_entity(e["entity_id"])
            count += 1
    print(f"✅ Cleanup complete. {count} entities removed.")

if __name__ == "__main__":
    time.sleep(10)
    cleanup()
