
import sys
import os
from lxml import html

URL_BASE = 'https://my.scouts.ie'
USERNAME = os.environ.get('SCOUTS_USERNAME')[1:]
PASSWORD = os.environ.get('SCOUTS_PASSWORD')
PROFILE_ID = os.environ.get('SCOUTS_PROFILE_ID')

def login(session):
    payload = {
        'username': USERNAME,
        'password': PASSWORD,
    }
    return session.post(URL_BASE + "/Account/Login", data=payload)

import requests
session = requests.Session()

print("~~~{}---".format(USERNAME), file=sys.stderr)
print(len(PASSWORD), file=sys.stderr)

result = login(session)
if result.status_code != 200:
    print('Failed to log in')
    sys.exit(1)

print(result, file=sys.stderr)
print(len(PROFILE_ID), file=sys.stderr)
result = session.get(URL_BASE + "/api/Training/GetProfileNextTraining?profileId={}".format(PROFILE_ID))
print(result.text)


