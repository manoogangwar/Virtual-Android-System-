import requests
import json

def get_system_info():
    """Retrieve mock system information from the virtual Android system."""
    system_info = {
        "device_id": "ANDROID-12345",
        "os_version": "9.0",
        "device_model": "Android-x86",
        "available_memory": "1024MB"
    }
    return system_info

def send_data_to_server():
    """Send mock system data to the backend API."""
    url = "http://127.0.0.1:8000/api/receive-data/"  # Change this to your actual API endpoint
    headers = {"Content-Type": "application/json"}
    system_info = get_system_info()
    
    print("Sending data to server...")
    response = requests.post(url, data=json.dumps(system_info), headers=headers)
    
    if response.status_code == 200:
        print("Server Response:", response.json())
    else:
        print(f"Failed to send data. Status Code: {response.status_code}")
        print("Response:", response.text)

if __name__ == "__main__":
    send_data_to_server()
