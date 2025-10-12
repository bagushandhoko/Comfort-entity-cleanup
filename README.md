# Comfort Entity Cleanup Add-on

### 🧹 Description
This Home Assistant add-on automatically removes all entities marked as **unavailable** (usually caused by deleted YAML files).  
It runs automatically at every system restart and can also be executed manually.

---

### ⚙️ Installation Steps

1. **Create a GitHub Repository**
   - Go to your GitHub account and create a new repository named:
     **bagushandhoko/comfort-entity-cleanup**
   - Do **not** initialize with README or license.

2. **Upload Files**
   - Extract this ZIP file locally.
   - Upload all files into your GitHub repository.

3. **Add Repository to Home Assistant**
   - In Home Assistant, open **Settings → Add-ons → Add-on Store**.
   - Click the **three-dot menu (⋮)** → **Repositories**.
   - Add this URL:
     ```
     https://github.com/bagushandhoko/comfort-entity-cleanup
     ```

4. **Install Add-on**
   - Find **Comfort Entity Cleanup** in the list.
   - Click **Install**.
   - Enable **Start on boot**, **Watchdog**, and **Auto update**.
   - Click **Start** to run manually if needed.

---

✅ Done! The add-on will now automatically clean up unavailable entities every restart.
