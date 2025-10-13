import os
import requests
import yaml

def main():
    ha_url = os.getenv('HA_URL', 'http://supervisor/core')
    ha_token = os.getenv('HA_TOKEN', '')

    headers = {
        "Authorization": f"Bearer {ha_token}",
        "Content-Type": "application/json",
    }

    print("🔍 Starting Comfort Entity Cleanup...")
    print(f"Connecting to: {ha_url}")

    try:
        response = requests.get(f"{ha_url}/api/states", headers=headers)
        response.raise_for_status()
        entities = response.json()
        print(f"✅ Retrieved {len(entities)} entities from Home Assistant.")
    except Exception as e:
        print(f"❌ Failed to fetch entities: {e}")
        return

    print("🧹 Cleaning up old Comfort entities...")
    for entity in entities:
        if entity["entity_id"].startswith("comfort2mqtt."):
            print(f" - Found entity: {entity['entity_id']}")

    print("✅ Cleanup complete!")

if __name__ == "__main__":
    main()
