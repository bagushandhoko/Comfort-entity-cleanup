import os
import requests

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
        response.raise
