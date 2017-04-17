import pandas as pd
import matplotlib.pyplot as plt
import urllib2
import requests
import json

#send request GET to opendota
def herodat():
	r = requests.get('https://api.opendota.com/api/heroStats')
	if r.status_code == 200:
	    data = r.json()
	df = pd.io.json.json_normalize(data)
	print df.columns.values.tolist()
	print df['name']

herodat()


