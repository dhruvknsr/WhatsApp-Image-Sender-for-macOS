import os
import time
import pyautogui
import subprocess

# Configuration - Edit these for your setup
GROUP_NAME = "Your Group Name"  # Exact group name
FOLDER_PATH = "/path/to/your/images/folder"  # e.g., "~/Screenshots"
IMAGE_EXTENSIONS = ('.jpg', '.jpeg', '.png')
MAX_MEDIA = 100  # WhatsApp limit; warn if exceeded

# Calibrated positions - Run calibrate_positions() to set these
SEARCH_CLICK_POS = (279, 93)  # Click position for search bar
GROUP_RESULT_POS = (300, 200)  # Position to click the group result
FILE_SELECTION_POS = (1200, 200)  # Drag start (center of selected files in Finder)
MSG_DROP_ZONE = (641, 577)  # Chat drop zone (center of open chat window)

# Fail-safe: Move mouse to top-left corner to abort
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.5  # Delay between actions

def calibrate_positions():
    """Run this to get mouse positions for your screen."""
    print("Hover over elements and note coordinates. Press Ctrl+C to stop.")
    print("1. Search bar in WhatsApp. 2. Group result (after typing name).")
    print("3. Center of file list in Finder (post-Cmd+A). 4. Chat drop zone.")
    try:
        while True:
            x, y = pyautogui.position()
            print(f"Current position: ({x}, {y})")
            time.sleep(1)
    except KeyboardInterrupt:
        print("Calibration done. Update positions above.")

# Open WhatsApp
applescript_open = '''
tell application "WhatsApp"
    activate
end tell
'''
subprocess.run(['osascript', '-e', applescript_open])
time.sleep(5)

# Search and open group
pyautogui.click(SEARCH_CLICK_POS)
time.sleep(1)
pyautogui.write(GROUP_NAME)
time.sleep(4)  # Wait for results
pyautogui.click(GROUP_RESULT_POS)
time.sleep(3)

# Get images count
images = [f for f in os.listdir(FOLDER_PATH)
          if f.lower().endswith(IMAGE_EXTENSIONS)]
num_images = len(images)
if num_images == 0:
    print("No images found.")
    exit()

print(f"Found {num_images} images. Selecting all and sending.")

if num_images > MAX_MEDIA:
    print(f"Warning: {num_images} > {MAX_MEDIA} limit.")

# Open Finder
subprocess.run(['open', FOLDER_PATH])
time.sleep(3)

# Select all and drag
pyautogui.hotkey('command', 'a')
time.sleep(1)
drop_zone = (MSG_DROP_ZONE[0], MSG_DROP_ZONE[1] - 50)
pyautogui.click(FILE_SELECTION_POS)
pyautogui.mouseDown(button='left')
pyautogui.dragTo(drop_zone[0], drop_zone[1], duration=1.5, button='left')
pyautogui.mouseUp(button='left')
time.sleep(3)

# Send
pyautogui.press('enter')
time.sleep(10)  # Wait for upload

print("All images sent successfully.")

# Close apps
applescript_close_whatsapp = '''
tell application "WhatsApp"
    quit
end tell
'''
subprocess.run(['osascript', '-e', applescript_close_whatsapp])
print("WhatsApp closed.")

applescript_close_finder = '''
tell application "Finder"
    close every window
end tell
'''
subprocess.run(['osascript', '-e', applescript_close_finder])
print("All Finder windows closed.")

# Uncomment to run calibration
# calibrate_positions()