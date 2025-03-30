import os

# Path to Android image file (Change this to your downloaded image path)
ANDROID_IMAGE = "android-x86_64.iso"

def launch_android():
    print("Starting Android Virtual System...")

    # QEMU command to start Android Emulator
    os.system(f"qemu-system-x86_64 -m 2048 -cdrom {ANDROID_IMAGE} -boot d -enable-kvm -smp 4 -net nic -net user -vga virtio")

if __name__ == "__main__":
    launch_android()
import os
import time

ANDROID_IMAGE = "android-x86_64.iso"
APK_PATH = "sample_app.apk"  # Path to the APK file

def launch_android():
    print("Starting Android Virtual System...")
    os.system(f"qemu-system-x86_64 -m 2048 -cdrom {ANDROID_IMAGE} -boot d -enable-kvm -smp 4 -net nic -net user -vga virtio")

def install_apk():
    print("Waiting for emulator to start...")
    time.sleep(30)  # Wait for the emulator to fully boot

    print("Installing APK...")
    os.system(f"adb install {APK_PATH}")
    print("APK installed successfully!")

if __name__ == "__main__":
    launch_android()
    install_apk()
    
    
    
    
    
    
def get_system_info():
    print("Retrieving system information...")
    
    os_version = os.popen("adb shell getprop ro.build.version.release").read().strip()
    device_model = os.popen("adb shell getprop ro.product.model").read().strip()
    available_memory = os.popen("adb shell cat /proc/meminfo | grep MemAvailable").read().strip()
    
    print(f"OS Version: {os_version}")
    print(f"Device Model: {device_model}")
    print(f"Available Memory: {available_memory}")

    with open("system_logs.txt", "w") as f:
        f.write(f"OS Version: {os_version}\n")
        f.write(f"Device Model: {device_model}\n")
        f.write(f"Available Memory: {available_memory}\n")

if __name__ == "__main__":
    launch_android()
    install_apk()
    get_system_info()

