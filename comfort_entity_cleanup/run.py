import os
import json

print("Addon Comfort Entity Cleanup dimulai...")

ha_config = "/config"
entities_path = os.path.join(ha_config, ".storage/core.entity_registry")

if not os.path.exists(entities_path):
    print("File entity_registry tidak ditemukan.")
else:
    print("Membersihkan entitas yang tidak terdaftar di YAML...")
    # logika pembersihan bisa ditambahkan di sini

print("Selesai.")
