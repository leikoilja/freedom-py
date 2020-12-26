from requests import Session


ENDPOINT_DEVICES = "https://freedom.to/devices/"
ENDPOINT_FILTERS = "https://freedom.to/filter_lists/"
ENDPOINT_SCHEDULES = "https://freedom.to/api/v1/schedules"


class FreedomClient(object):
    """
    This is the entry point to using the API.
    Create an instance of this class, passing it the value of the
    "token" for Freedom.to.

    Note for input arguments:
    token must be a long-lived access token.
    device_ids must be a list of user devices.
    """

    def __init__(
        self,
        token,
        device_ids,
    ):
        self.session = Session()
        headers = {'Authorization': f"Bearer {token}"}
        self.session.headers.update(headers)
        self.device_ids = device_ids;

    def activate_session(self, duration_sec, filter_list_ids):
        data = {
            "device_ids": self.device_ids,
            "start_time": "now",
            "filter_list_ids": filter_list_ids,
            "duration": duration_sec
        }
        self.session.post(ENDPOINT_SCHEDULES, json=data, verify=False)

    def _get_devices(self):
        response = self.session.get(ENDPOINT_DEVICES)
        return response.json()

    def get_device_ids(self):
        devices = self._get_devices()['devices']
        ids = [device['id'] for device in devices]
        return ids

    def _get_filters(self):
        response = self.session.get(ENDPOINT_FILTERS)
        return response.json()

    def get_filter_ids(self):
        filters = self._get_filters()['filter_lists']
        ids = [filter['id'] for filter in filters]
        return ids
