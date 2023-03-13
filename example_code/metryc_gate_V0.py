import sys
import requests
import random
import json
import time
import pandas as pd

from auth import get_access_token

lats= [25.80665]
lons= [-80.12412]
access_token = get_access_token()
## API query
def metryc_point (access_token, lats, lons, tag=None):

    if type(lats) != type([]):
        lats = [lats]
        lons = [lons]

    url = 'https://api.reask.earth/v1/metryc/gate'
    params = {
        'access_token': access_token,
        'peril': 'TC_Wind',
        'gate': 'circle',
        'lats': lats,
        'lons': lons,
        'radius_km': 50
    }

    if tag is not None:
        params['tag'] = tag
    
    start_time = time.time()
    res = requests.get(url, params=params)
    print(res.status_code)
    if res.status_code != 200:
        print(res.text)
        return None

    return res.json()

if __name__ == '__main__':
    sys.exit(metryc_point (access_token , [25.80665],[-80.12412]))