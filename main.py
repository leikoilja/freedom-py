from os import getenv
from freedom.client import FreedomClient


# Make sure to have environment variable TOKEN
# Or simply hardcode your token here
token = getenv('TOKEN')

# List of device ids that will be blocked
device_ids = [
    getenv('USER_1_IOS'),
    getenv('USER_1_MAC'),
    getenv('USER_2_IOS'),
    getenv('USER_2_MAC')
]

client = FreedomClient(token=token, device_ids=device_ids)

# List of filter ids to apply for a block
filter_list_ids = [
    getenv('FILTER_1'),
    getenv('FILTER_2'),
]

# Activate distraction-free session
client.activate_session(duration_sec=10, filter_list_ids=filter_list_ids)
