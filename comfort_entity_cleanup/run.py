import os
import json
import requests

# URL HA Supervisor
HA_URL = os.environ.get("HA_URL", "http://supervisor/core")
HA_TOKEN = os.environ.get("HA_TOKEN", "")

HEADERS = {
    "Authorization": f"Bearer {HA_TOKEN}",
    "Content-Type": "application/json",
}

def get_entities():
    r = requests.get(f"{HA_URL}/api/states", headers=HEADERS)
    return r.json() if r.status_code == 200 else []

def load_yaml_entities():
    yaml_folder = "/app/yaml"
    entities = set()
    for root, dirs, files in os.walk(yaml_folder):
        for file in files:
            if file.endswith(".yaml"):
                with open(os.path.join(root, file), "r") as f:
                    for line in f:
                        if line.strip().startswith("name:"):
                            name = line.split(":", 1)[1].strip().strip('"')
                            entities.add(name)
    return entities

def remove_unavailable_entities():
    yaml_entities = load_yaml_entities()
    ha_entities = get_entities()
    removed = []
    for e in ha_entities:
        entity_id = e["entity_id"]
        state = e.get("state")
        if state == "unavailable":
            # hapus kalau tidak ada di yaml
            if entity_id not in yaml_entities:
                resp = requests.delete(f"{HA_URL}/api/states/{entity_id}", headers=HEADERS)
                if resp.status_code == 200:
                    removed.append(entity_id)
    return removed

if __name__ == "__main__":
    removed_entities = remove_unavailable_entities()
    print(f"Removed entities: {removed_entities}")
