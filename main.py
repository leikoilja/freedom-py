from os import getenv
from freedom.client import FreedomClient


# Make sure to have environment variable TOKEN
token = getenv('TOKEN')

# If you dont have a token you can get it using get_token method and save it under environment variables
# Note: to avoid problems it's recommended you get a token just once and then reuse it
#
# EMAIL = 'example@example.com'
# PASSWORD = 'password'
# token = client.get_token(email=EMAIL, password=PASSWORD))

# List of device ids that will be blocked
device_ids = [
    getenv('USER_1_IOS'),
    getenv('USER_1_MAC'),
    getenv('USER_2_IOS'),
    getenv('USER_2_MAC')
]

# Or get all your device_ids.
# When running this method it will print out the list of IDS and device names on
# the screen. The method returns only device ids
#
# device_ids = client.get_device_ids()

client = FreedomClient(token=token, device_ids=device_ids)

# List of filter ids to apply for a block
filter_list_ids = [
    getenv('FILTER_1'),
    getenv('FILTER_2'),
]

# Or get all your filter_ids.
# When running this method it will print out the list of IDS and filter names on
# the screen. The method returns only filter ids
#
# filter_ids = client.get_filter_ids()

# Activate distraction-free session
client.activate_session(duration_sec=10, filter_list_ids=filter_list_ids)
