#!/usr/bin/env bash
set -e

echo "=== Comfort Entity Cleanup Add-on ==="
echo "📦 Membuat backup core.entity_registry & restore_state..."
cp /config/.storage/core.entity_registry /config/.storage/core.entity_registry.backup || true
cp /config/.storage/core.restore_state /config/.storage/core.restore_state.backup || true

echo "🧹 Menghapus entitas Comfort dari registry..."
python3 - <<'PYCODE'
import json, re, os

entity_file = "/config/.storage/core.entity_registry"
if not os.path.exists(entity_file):
    print("❌ File entity_registry tidak ditemukan.")
    exit(1)

with open(entity_file, "r", encoding="utf-8") as f:
    data = json.load(f)

before = len(data["data"]["entities"])
data["data"]["entities"] = [
    e for e in data["data"]["entities"]
    if not re.search(r"comfort", e["entity_id"], re.IGNORECASE)
]
after = len(data["data"]["entities"])
deleted = before - after

with open(entity_file, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print(f"✅ {deleted} entitas Comfort dihapus dari registry.")
print("🔄 Silakan restart Home Assistant agar perubahan diterapkan.")
PYCODE
