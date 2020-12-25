import requests
import os


DEVICES = [
    os.getenv('USER_1_IOS'),
    os.getenv('USER_1_MAC'),
    os.getenv('USER_2_IOS'),
    os.getenv('USER_2_MAC'),
]
DURATION = 30
ENDPOINT = "https://freedom.to/api/v1/schedules"
FILTERS = [
    os.getenv('FILTER_1'),
    os.getenv('FILTER_2'),
]
TOKEN = "Bearer "+os.getenv('TOKEN')
HEADERS = {"Authorization": TOKEN}

data = {
    "device_ids": DEVICES,
    "start_time": "now",
    "filter_list_ids": FILTERS,
    "duration": DURATION
}

request = requests.post(ENDPOINT, json=data, headers=HEADERS, verify=False)

if request.status_code not in [200,201]:
    print(f"Failed to enable Freedom with error code {request.status_code}")
