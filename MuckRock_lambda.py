import json
import requests
from datetime import datetime
import dateutil.relativedelta
import os 

username = os.environ['my_username']
passphrase = os.environ['my_passphrase']
api_url = 'https://www.muckrock.com/api_v1/'

response = requests.post('https://www.muckrock.com/api_v1/token-auth/',
                         data={'username': username, 'password': passphrase })
data = response.json()
token = data['token']
print('Token received from MR successfully')


def get_headers(token=None):
    if token:
        return {
        'Authorization': 'Token %s' %token,
        'content-type': 'application/json'
        }
    else:
        return {'content-type': 'application/json'}


def lambda_handler(event, context): 
    print("Received event")
    # first get today's month then subtract one month to grab previous

    s = str(datetime.now())[0:10]
    d = datetime.strptime(s, "%Y-%m-%d")
    d2 = d - dateutil.relativedelta.relativedelta(months=1)
    # strip day of the week + other timedate objects
    d2 = str(d2)[0:7]

    # use test agencies from MuckRock
    foia_doc = json.dumps({
        'jurisdiction': 10,
        'agency': 248,
        'title': 'Last Month\'s 1505 checks',
        'document_request':
            'For the year and month of ' + d2 +
            ', I am requesting a list of all 1505 checks expenditures issues by the Bureau of Organized Crime. '
            'I am requesting the full list of checks spent by the BoC during the full month of ' + d2 + '. ',
        })
                                                                                                                        
    header = get_headers(token)
    foia_url = api_url+'foia/'
    r = requests.post(foia_url, data=foia_doc, headers=header)
    print(r.text)
    print(r.status_code)
    print('All done')
