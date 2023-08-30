
import sys
import os
from argparse import ArgumentParser
from lxml import html

URL_BASE = 'https://my.scouts.ie'
PROFILE_ID = os.environ.get('SCOUTS_PROFILE_ID')
USERNAME = os.environ.get('SCOUTS_USERNAME')
PASSWORD = os.environ.get('SCOUTS_PASSWORD')

parser = ArgumentParser()
parser.add_argument('--activity', action='store_true')
args = parser.parse_args()

URL_ACTION = "Training/GetProfileNextTraining" if not args.activity else "Activity/GetProfileNextActivity"

def login(session):
    payload = {
        'username': USERNAME,
        'password': PASSWORD,
    }
    return session.post(URL_BASE + "/Account/Login", data=payload)

import requests
session = requests.Session()

result = login(session)
if result.status_code != 200:
    print('Failed to log in')
    sys.exit(1)


result = session.get(URL_BASE + "/api/{}?profileId={}".format(URL_ACTION, PROFILE_ID))

if result.status_code == 200:
    print('Success! Response length is {}'.format(len(result.text)), file=sys.stderr)
else:
    print('Failed! Response code is {}'.format(result.status_code), file=sys.stderr)

print(result.text)
