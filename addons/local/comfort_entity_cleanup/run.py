import os
import requests
import json

def main():
    ha_url = os.getenv("HA_URL", "http://supervisor/core")
    ha_token = os.getenv("HA_TOKEN", "")

    headers = {
        "Authorization": f"Bearer {ha_token}",
        "Content-Type": "application/json",
    }

    print("🔍 Starting Comfort Entity Cleanup...")
    print(f"Connecting to Home Assistant API at {ha_url}")

    try:
        response = requests.get(f"{ha_url}/api/states", headers=headers)
        response.raise_for_status()
        entities = response.json()
        print(f"✅ Retrieved {len(entities)} entities from Home Assistant.")
    except Exception as e:
        print(f"❌ Failed to fetch entities: {e}")
        return

    comfort_entities = [
        e["entity_id"] for e in entities if e["entity_id"].startswith("comfort2mqtt.")
    ]

    if not comfort_entities:
        print("✅ No comfort2mqtt entities found.")
        return

    print(f"🧹 Found {len(comfort_entities)} comfort2mqtt entities. Checking registry...")

    try:
        registry_url = f"{ha_url}/api/config/entity_registry/list"
        reg_response = requests.get(registry_url, headers=headers)
        reg_response.raise_for_status()
        registry_entities = reg_response.json()
    except Exception as e:
        print(f"❌ Failed to read entity registry: {e}")
        return

    registry_ids = {e["entity_id"] for e in registry_entities}
    removed = 0

    for eid in comfort_entities:
        if eid not in registry_ids:
            print(f"⚠️ {eid} missing from registry, skipping...")
            continue

        try:
            # Hapus entitas dari registry
            print(f"🗑️ Deleting {eid} from registry...")
            delete_url = f"{ha_url}/api/config/entity_registry/{eid}"
            del_resp = requests.delete(delete_url, headers=headers)
            if del_resp.status_code in (200, 202, 204):
                print(f"✅ Deleted: {eid}")
                removed += 1
            else:
                print(f"⚠️ Failed to delete {eid}: {del_resp.status_code} {del_resp.text}")
        except Exception as e:
            print(f"❌ Error deleting {eid}: {e}")

    print(f"✅ Cleanup complete! {removed} entities removed.")

if __name__ == "__main__":
    main()
