import io
import pandas as pd
import matplotlib.pyplot as plt
import requests
import os
import json
from datetime import date as dt, timedelta
import matplotlib.dates as mdates


BTP_BUND_API_KEY = os.environ['CS_BTP_BUND_API_KEY]

from datetime import date as dt, timedelta
end = dt.today()
start = end - timedelta(days=365)

timeseries_url = "https://bonds-api.com/api/v1/timeseries"

DE_params = {'country'  : 'DE',
            'maturity' : '10Y',
            'start' : start,
            'end' : end,
            'api_key': BTP_BUND_API_KEY}
          
DE_response = requests.get(timeseries_url, DE_params, headers={'Accept': 'application/json'})
DE_data = DE_response.json()

IT_params = {'country'  : 'IT',
          'maturity' : '10Y',
          'start' : start,
          'end' : end,
          'api_key': BTP_BUND_API_KEY}
          
IT_response = requests.get(timeseries_url, IT_params, headers={'Accept': 'application/json'})
IT_data = IT_response.json()

print(json.dumps(DE_data, indent=2))
print(json.dumps(IT_data, indent=2))
