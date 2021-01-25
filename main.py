import argparse

from os import getenv
from freedom.client import FreedomClient

parser = argparse.ArgumentParser()

parser.add_argument(
    "-t",
    "--token",
    help = "Freedom Token"
)
parser.add_argument(
    "-d",
    "--duration",
    help = "Session duration in seconds"
)
parser.add_argument(
    "--device-uids",
    nargs="+",
    help = "List of device UIDs"
)
parser.add_argument(
    "--filter-uids",
    nargs="+",
    help = "List of filter UIDs"
)

args = parser.parse_args()

# If you dont have a token you can get it using get_token method and save it under environment variables
# Note: to avoid problems it's recommended you get a token just once and then reuse it
#
# EMAIL = 'example@example.com'
# PASSWORD = 'password'
# token = client.get_token(email=EMAIL, password=PASSWORD))

# Make sure to have environment variable TOKEN or pass it as argument
token = getenv('TOKEN', args.token)

duration = args.duration or 10

# List of device ids that will be blocked
device_ids = []

for device_id in [
        getenv('USER_1_IOS'),
        getenv('USER_1_MAC'),
        getenv('USER_2_IOS'),
        getenv('USER_2_MAC')
    ]:
    if device_id:
        device_ids.append(device_id)

device_ids = args.device_uids if not device_ids else device_ids

# Or get all your device_ids.
# When running this method it will print out the list of IDS and device names on
# the screen. The method returns only device ids
#
# device_ids = client.get_device_ids()

if token and device_ids:
    client = FreedomClient(token=token, device_ids=device_ids)
else:
    raise Exception("You must provide TOKEN and device_uids. See help [-h]")

# List of filter ids to apply for a block
filter_ids = []

for filter_id in [
        getenv('FILTER_1'),
        getenv('FILTER_2'),
    ]:
    if filter_id:
        filter_ids.append(filter_id)

filter_ids = args.filter_uids if not filter_ids else filter_ids

# Or get all your filter_ids.
# When running this method it will print out the list of IDS and filter names on
# the screen. The method returns only filter ids
#
# filter_ids = client.get_filter_ids()

# Activate distraction-free session
if filter_ids:
    client.activate_session(duration_sec=duration, filter_list_ids=filter_ids)
else:
    raise Exception("You must provide filter_uids. See help [-h]")
