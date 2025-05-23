# Virtual Android System Simulation

This script creates a virtual Android system using QEMU, installs an APK, and retrieves system information.

## **Prerequisites**
1. **Install QEMU**  
   - Download from: [https://www.qemu.org/download/](https://www.qemu.org/download/)
   - Add QEMU to system PATH.

2. **Install ADB (Android Debug Bridge)**  
   - Download ADB tools: [https://developer.android.com/studio/releases/platform-tools](https://developer.android.com/studio/releases/platform-tools)
   - Add ADB to system PATH.

3. **Download Android-x86 ISO**  
   - Get it from: [https://www.android-x86.org/download](https://www.android-x86.org/download)
   - Place `android-x86_64.iso` in the same directory as this script.

4. **Prepare APK for Installation**  
   - Rename the APK file to `sample_app.apk`.
   - Place it in the same directory as this script.

## **How to Run**
1. Open **Git Bash / Command Prompt** in the project folder.
2. Run the script:
   ```bash
   python android_emulator.py









# Android Networking Script

This script establishes an HTTP connection between a virtual Android system and a backend API.

## **🔹 How It Works**
1. Retrieves **mock system information**:
   - Device ID
   - OS Version
   - Device Model
   - Available Memory
2. Sends this data to the backend API (`http://127.0.0.1:8000/api/receive-data/`).
3. Logs the **server’s response**.

## **📌 Prerequisites**
- Ensure your backend API is running (Django/Flask).
- Install `requests` module (if not installed):
  ```bash
  pip install requests

