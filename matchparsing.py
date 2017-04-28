#match parsing

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

import requests
import json
import datetime as dt

match_id = 3142390443
column_list = ['radiant_team.name','dire_team.name','first_blood_time','teamfights','leagueid']

r = requests.get('https://api.opendota.com/api/matches/3142390443') #send request GET to opendota

if r.status_code == 200:
	data = r.json()
df = pd.io.json.json_normalize(data)

print df.columns.values.tolist()
for i in len(column_list):
	print column_list[i]
