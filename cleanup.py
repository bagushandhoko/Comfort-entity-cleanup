import os
import requests

def main():
    ha_url = os.getenv('HA_URL', 'http://supervisor/core')
    ha_token = os.getenv('HA_TOKEN', '')

    headers = {
        "Authorization": f"Bearer {ha_token}",
        "Content-Type": "application/json",
    }

    print("🔍 Menghubungkan ke:", ha_url)
    try:
        resp = requests.get(f"{ha_url}/api/states", headers=headers)
        resp.raise_for_status()
        entities = resp.json()
        print(f"✅ {len(entities)} entitas ditemukan.")
    except Exception as e:
        print(f"❌ Gagal mengambil entitas: {e}")
        return

    for e in entities:
        if e["entity_id"].startswith("comfort2mqtt."):
            print(f"🧹 Menemukan entitas: {e['entity_id']}")

    print("🎯 Pembersihan selesai.")

if __name__ == "__main__":
    main()
