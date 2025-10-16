import os
import requests

def main():
    ha_url = os.getenv("HA_URL", "http://supervisor/core")
    ha_token = os.getenv("HA_TOKEN", "")
    headers = {
        "Authorization": f"Bearer {ha_token}",
        "Content-Type": "application/json",
    }
    print("Connecting to HA:", ha_url)
    try:
        resp = requests.get(f"{ha_url}/api/states", headers=headers)
        resp.raise_for_status()
        entities = resp.json()
        print(f"Number of entities: {len(entities)}")
    except Exception as e:
        print("Error fetching entities:", e)
        return
    for e in entities:
        if e["entity_id"].startswith("comfort2mqtt."):
            print("Found:", e["entity_id"])
    print("Done.")

if __name__ == "__main__":
    main()
