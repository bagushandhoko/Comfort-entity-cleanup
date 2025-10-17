#!/usr/bin/env python3
import os
import json
import requests
from datetime import datetime

HA_API_URL = "http://supervisor/core/api"
HEADERS = {
    "Authorization": f"Bearer {os.getenv('SUPERVISOR_TOKEN')}",
    "Content-Type": "application/json"
}

def ha_get(path):
    r = requests.get(f"{HA_API_URL}/{path}", headers=HEADERS)
    r.raise_for_status()
    return r.json()

def ha_post(path, payload):
    r = requests.post(f"{HA_API_URL}/{path}", headers=HEADERS, json=payload)
    if r.status_code not in (200, 201):
        print(f"⚠️ POST {path} failed: {r.status_code}")
    return r

def backup_file(src):
    if os.path.exists(src):
        ts = datetime.now().strftime("%Y%m%d-%H%M%S")
        backup = f"{src}.backup-{ts}"
        with open(src, "r") as f:
            content = f.read()
        with open(backup, "w") as f:
            f.write(content)
        print(f"📦 Backup dibuat: {backup}")

def main():
    print("=== Comfort Entity Cleanup (Add-on version) ===")

    core_registry = "/config/.storage/core.entity_registry"
    restore_registry = "/config/.storage/core.restore_state"

    # Backup file
    backup_file(core_registry)
    backup_file(restore_registry)

    with open(core_registry, "r") as f:
        data = json.load(f)

    entities = data.get("data", {}).get("entities", [])
    before = len(entities)

    new_entities = [
        e for e in entities
        if not (
            e.get("entity_id", "").startswith("binary_sensor.comfort_")
            or e.get("entity_id", "").startswith("sensor.comfort_")
            or e.get("entity_id", "").startswith("switch.comfort_")
            or e.get("entity_id", "").startswith("update.comfort_")
        )
    ]

    deleted = before - len(new_entities)
    data["data"]["entities"] = new_entities

    with open(core_registry, "w") as f:
        json.dump(data, f, indent=2)

    print(f"✅ {deleted} entitas Comfort dihapus.")
    print("🔄 Restart Home Assistant agar perubahan diterapkan.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"❌ Error: {e}")
