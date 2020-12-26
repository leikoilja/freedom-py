# Freedom-py

Unofficial Python 3 client for [freedom.to](https://freedom.to/) API
that blocks distracting websites and apps on your Mac, Windows, Android, iOS.

Currently supported features:
- Activate Freedom session by specifying devices, filters and block duration

# Usage

## Quickstart

Note: the package was written and tested on Python 3.

- Clone the repo
- Install dependency packages: `pip install requests`

```Python
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
```

Please note that this example uses various environmental variables like your
long-lived token, device ids and filter ids.
You can either set those up in your `.env` file or lookup how to set
environmental variables for your operating system. Worst case you can always
hardcode your values there :)

# Development
If there are missing features please open a new issue with feature request.
PRs are very welcomed.

# TODO
- [ ] Write a paragraph how to easily find one's authentication TOKEN
- [ ] Implement GET request to fetch and show device ids
- [ ] Implement GET request to fetch and show filter ids
