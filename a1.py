import requests
import unittest
from common import re_data_yaml

host = re_data_yaml.get_host()
url = host + "/api/user_access_lock_data"
par = {
    "member_id": 1618
}
r = requests.get(url, params=par)
result = r.json()["data"]
print(result)
print(type(result))