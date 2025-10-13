import os
import time

def main():
    print("🔧 Comfort Entity Cleanup add-on started.")
    ha_url = os.getenv("HA_URL", "http://supervisor/core")
    token = os.getenv("HA_TOKEN", "")
    print(f"Connected to Home Assistant at {ha_url}")
    if not token:
        print("⚠️  Warning: HA_TOKEN not set. Please configure it in add-on options.")
    while True:
        print("🧹 Running cleanup task... (placeholder)")
        time.sleep(30)

if __name__ == "__main__":
    main()
