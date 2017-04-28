#tournamentmining
import pandas as pd

import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

import requests
import json
import datetime as dt

# get requests

Kiev_major = 5157 #leagueid

id_list = []

def promatch():
	r = requests.get('https://api.opendota.com/api/proMatches')
	if r.status_code == 200:
	    data = r.json()
	df = pd.io.json.json_normalize(data)
	print df.columns.values.tolist()
	#reformat the pro matches data frame
	match = pd.DataFrame()
	match = match.append(df['radiant_name'])
	match = match.append(df['dire_name'])
	match = match.append(df['duration']) #data is in second, not MM:SS format
	match = match.append(df['radiant_win'])
	match = match.append(df['leagueid'])
	#print and return
	return match

print promatch()

def durationmean():
	pass

def findleague(id_list):
	for i in range(len(id_list)):
		#parse match by id
		if (data['leagueid'] == Kiev_major):
			match = match.append()

		pass
	