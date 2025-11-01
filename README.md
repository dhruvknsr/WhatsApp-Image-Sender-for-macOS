# WhatsApp Image Sender for macOS

Automate sending images (e.g., screenshots) from a folder to a **WhatsApp group** using **WhatsApp Desktop** on macOS.  
This script leverages **PyAutoGUI** for GUI automation and **AppleScript** for app control. 
Supports **headless setups** on Mac Mini with a dummy HDMI plug.

---

## 🚀 Features

✅ Opens WhatsApp, searches for a specific group, and sends **all images in a folder** as a single batch.  
✅ Uses **Cmd+A in Finder** for easy multi-file selection and drag-to-chat.  
✅ Includes post-send cleanup: **Quits WhatsApp and closes Finder windows.**  
✅ Built-in **calibration function** for mouse positions (adapts to different resolutions).  
✅ **Cron-ready** for scheduled execution (e.g., daily at 9:00 AM).  
✅ Handles up to WhatsApp's **100-media limit**, with warnings for larger batches.  
✅ **Logs output** for easy debugging in automated runs.

---

## 🧩 Requirements

- **macOS 11+ (Big Sur or later)**
- **Python 3.9+** (installed via Homebrew).  
- **WhatsApp Desktop app** (free from Mac App Store) with an active logged-in session.  
- For headless use (Mac Mini, etc.): **Dummy HDMI plug** (4K emulator, ~$10).  
- Permissions:  
  - ✅ Enable **Accessibility**  
  - ✅ Enable **Screen Recording**  
  *(System Settings → Privacy & Security)*  
- Optional: **Parsec** or **VNC** for remote monitoring on headless setups.

---

## ⚙️ Installation

### 1️⃣ Install Homebrew

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### 2️⃣ Install Python

```bash
brew install python
```

Verify installation:

```bash
which python3
```

Expected path (Apple Silicon): `/opt/homebrew/bin/python3`

---

### 3️⃣ Install Dependencies

```bash
/opt/homebrew/bin/python3 -m pip install --upgrade pip
/opt/homebrew/bin/python3 -m pip install pyautogui
```

*(Intel Macs: replace `/opt/homebrew/` with `/usr/local/`)*

---

### 4️⃣ (Optional) Create a Virtual Environment

```bash
/opt/homebrew/bin/python3 -m venv venv
source venv/bin/activate
pip install pyautogui
```

Deactivate when done:

```bash
deactivate
```

---

### 5️⃣ Clone or Download the Repo

```bash
git clone https://github.com/dhruvknsr/whatsapp-image-sender-macos.git
cd whatsapp-image-sender-macos
```

Or download **`whatsapp_image_sender_macos.py`** directly.

---

## ⚙️ Configuration

Open the script and modify these variables:

```python
GROUP_NAME = "YOUR GROUP NAME"  # Your WhatsApp group name
FOLDER_PATH = "/path/to/your/folder"
IMAGE_EXTENSIONS = ('.jpg', '.jpeg', '.png')
MAX_MEDIA = 100  # WhatsApp's limit
```

---

### 🖱️ Calibrate Mouse Positions

Run the calibration function (uncomment `calibrate_positions()` at the end of the script).

Hover over and record these points:

1. **WhatsApp search bar**
2. **Group result** (after typing name)
3. **Finder file list center** (after Cmd+A)
4. **Chat drop zone**

Example for 1440×900 resolution:

```python
SEARCH_CLICK_POS = (279, 93)
GROUP_RESULT_POS = (300, 200)
FILE_SELECTION_POS = (1200, 200)
MSG_DROP_ZONE = (641, 577)
```

💡 Use **Finder > View > as List** for consistent file spacing.

---

## ▶️ Usage

### Manual Execution

Ensure WhatsApp is open and logged in.

```bash
/opt/homebrew/bin/python3 whatsapp_image_sender_macos.py
```

With virtual environment:

```bash
source venv/bin/activate
python whatsapp_image_sender_macos.py
```

Expected output:

```
Found X images
All images sent successfully.
```

---

### Logging Example

Keep the system awake and log output:

```bash
caffeinate -t 300 /opt/homebrew/bin/python3 whatsapp_image_sender_macos.py >> output.log 2>&1
```

Check log:

```bash
cat output.log
# or
tail -f output.log
```

---

### Add Test Images

To test safely, add 1–5 `.jpg` or `.png` files to your folder.

---

## 🕒 Scheduling with Cron

Automate daily runs at **9:00 AM**:

```bash
crontab -e
```

Add this line:

```bash
0 9 * * * caffeinate -t 300 /opt/homebrew/bin/python3 /path/to/whatsapp_image_sender_macos.py >> /path/to/log.txt 2>&1
```

- `0 9 * * *`: Every day at 9:00 AM  
- `0 9 * * 1-5`: Weekdays only  
- Log file tracks all outputs and errors.

Check cron jobs:

```bash
crontab -l
```

Simulate a test run:

```bash
echo 'caffeinate -t 300 /opt/homebrew/bin/python3 /path/to/script.py' | at now +1 minute
```

---

### 🧠 For Headless Mac Mini

- Insert **dummy HDMI plug**  
- Monitor via Parsec or Screen Sharing  
- Enable **auto-login** under:  
  *System Settings → Users → Login Options*  
- Use `caffeinate` to prevent sleep.

---

## ⚠️ Limitations

- GUI-dependent — may need recalibration after macOS updates.  
- WhatsApp limits: **100 images per batch**.  
- Requires dummy HDMI for headless setups.  
- Cron needs **active user session** with granted permissions.  
- macOS-only (PyAutoGUI + AppleScript are platform-specific).

---

## 🧰 Troubleshooting

| Issue | Solution |
|-------|-----------|
| `ModuleNotFoundError: pyautogui` | Reinstall with correct Python path |
| Mouse clicks/drag miss | Recalibrate positions; increase `time.sleep()` duration |
| Apps don’t open/close | Test AppleScript: `osascript -e 'tell app "WhatsApp" to quit'` |
| Cron not running | Add `export PATH="/opt/homebrew/bin:$PATH"` to `~/.zshrc` |
| No images sent | Check folder path and file permissions |
| Headless fails | Verify HDMI dummy plug via `system_profiler SPDisplaysDataType` |

---

## 🤝 Contributing

1. Fork this repository.  
2. Create your feature branch:

   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. Commit your changes:

   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. Push the branch:

   ```bash
   git push origin feature/AmazingFeature
   ```
5. Open a Pull Request!

---

## 🐞 Reporting Bugs

Open an **Issue** and include:
- Log output  
- macOS version  
- Python version  
- Screenshot (if possible)

---

## 🧑‍💻 Author

**Dhruv Kansara**  
📧 [dhruvknsr@gmail.com](mailto:dhruvknsr@gmail.com)

---

## 📜 License

MIT License © 2025 Dhruv Kansara  
Use freely with attribution.