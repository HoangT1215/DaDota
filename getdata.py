import pandas as pd
import matplotlib.pyplot as plt
import urllib2
import requests
import json

patch = '7.05'
n_hero = 110

#send request GET to opendota
def herodat():
	r = requests.get('https://api.opendota.com/api/heroStats')
	if r.status_code == 200:
	    data = r.json()
	df = pd.io.json.json_normalize(data)
	print df.columns.values.tolist() # print out the columns
	# the names are actually too long, probably will use id afterwards

	answer = [] # depends on what kind of data we want, we need a separate answer
	# win-rate
	for i in range (n_hero):
		pass

	# ban/pick

	# game-time

	return answer

def teamdat():
	r = requests.get('https://api.opendota.com/api/teams')
	if r.status_code == 200:
	    data = r.json()
	df = pd.io.json.json_normalize(data)
	print df.columns.values.tolist()
	print df['name']

	
teamdat()


