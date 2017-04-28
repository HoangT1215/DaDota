from __future__ import division

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

import requests
import json
import datetime as dt



patch = '7.05'
n_hero = 113
team_name = 'Invictus Gaming' #instead of a specific team name, I can make a list and let the script runs through it

#the functions

def herodat():
	r = requests.get('https://api.opendota.com/api/heroStats') #send request GET to opendota
	if r.status_code == 200:
	    data = r.json()
	df = pd.io.json.json_normalize(data)
	print df.columns.values.tolist() # print out the columns
	# the names are actually too long, probably will use id afterwards

	print df['id']
	answer = pd.DataFrame() # depends on what kind of data we want, we need a separate answer
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
	print df['tag']
	
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
	#print and return
	return match

def durationmean(data,n):
	s = 0
	count = 0
	print data.shape
	for i in range(n):
		s += data[i]['duration']
	return float(s/n)

def findteam(data,team): #find matches by team name
	sample = pd.DataFrame()
	for i in range(data.shape[1]):
		if (data[i]['radiant_name'] == team) or (data[i]['dire_name'] == team):
			sample = sample.append(data[i])
	return sample

# *** ===== ***
hero = pd.DataFrame()
data = promatch()
print data
demo = findteam(data = data, team = team_name)
print demo # demo and data are not the same

print durationmean(data, data.shape[0])
# *** plotting ***
