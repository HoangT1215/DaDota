#match parsing
import pandas as pd

import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

import requests
import json
import datetime as dt

match_id = [3142390443, 3144097046, 3144175535, 3142994571]

column_list = ['players','radiant_team.name','dire_team.name','first_blood_time','teamfights','leagueid']

def first_blood(match_id):
	s = 'https://api.opendota.com/api/matches/' + str(match_id)
	r = requests.get(s) #send request GET to opendota
	if r.status_code == 200:
		data = r.json()
	return data['first_blood_time']

def cour_kill(match_id):
	s = 'https://api.opendota.com/api/matches/' + str(match_id)
	r = requests.get(s) #send request GET to opendota
	if r.status_code == 200:
		data = r.json()
	cour1 = 0
	cour2 = 0
	for i in range(4):
		cour1 += (data['players'][i]['courier_kills'])
	for i in range(9):
		cour2 += (data['players'][i]['courier_kills'])
	cour2 = cour2 - cour1
	return (cour1,cour2)


def towerdam(match_id):
	s = 'https://api.opendota.com/api/matches/' + str(match_id)
	r = requests.get(s) #send request GET to opendota
	if r.status_code == 200:
		data = r.json()
	result = []
	for i in range(10):
		result.append([data['players'][i]['tower_damage'],data['players'][i]['name']])
	return result # a list of tower damage by players
