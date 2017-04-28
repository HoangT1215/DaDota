#tournamentmining
import pandas as pd

import numpy as np
import matchparsing

import matplotlib.pyplot as plt
import seaborn as sns

import requests
import json
import datetime as dt

from urllib import quote

# get requests

Kiev_major = 5157 #leagueid

id_list = []

sql = quote('''
  SELECT *
  FROM heroes 
  LEFT JOIN 
  (SELECT hero_id as id, count(*) matches, sum(case when (player_matches.player_slot < 128) = radiant_win then 1 else 0 end) wins
  FROM player_matches 
  JOIN matches USING(match_id) 
  WHERE leagueid = {}
  GROUP BY hero_id)
  herodata USING(id)
  ORDER BY matches desc''')

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

def findleague(id_list):
	for i in range(len(id_list)):
		#parse match by id
		if (data['leagueid'] == Kiev_major):
			match = match.append()

	pass
	
def get_ID():
	r = requests.get(sql)
	if r.status_code == 200:
	    data = r.json()
	
