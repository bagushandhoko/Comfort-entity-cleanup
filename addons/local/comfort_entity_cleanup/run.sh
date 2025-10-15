#!/bin/bash
echo "=== Comfort Entity Cleanup Add-on Starting ==="

if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 not found in container!"
    exit 1
fi

echo "✅ Python3 detected, running cleanup..."
python3 /app/run.py

echo "=== Comfort Entity Cleanup Finished ==="
