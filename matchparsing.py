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
	for i in range(5):
		cour1 += (data['players'][i]['courier_kills'])
	for i in range(10):
		cour2 += (data['players'][i]['courier_kills'])
	cour2 = cour2 - cour1
	return (cour1,cour2)

def kills_per_min(match_id):
	pass

def towerdam(match_id):
	s = 'https://api.opendota.com/api/matches/' + str(match_id)
	r = requests.get(s) #send request GET to opendota
	if r.status_code == 200:
		data = r.json()
	result = []
	for i in range(10):
		result.append([data['players'][i]['tower_damage'],data['players'][i]['name']])
	return result # a list of tower damage by players

def purchase_log():
	pass

def goldadv(match_id): # data will be updated every minute, so we can graph the data
	s = 'https://api.opendota.com/api/matches/' + str(match_id)
	r = requests.get(s) #send request GET to opendota
	if r.status_code == 200:
		data = r.json()
	return data['radiant_gold_adv']

def camps_stacked(match_id):
	s = 'https://api.opendota.com/api/matches/' + str(match_id)
	r = requests.get(s) #send request GET to opendota
	if r.status_code == 200:
		data = r.json()
	camp1 = 0
	camp2 = 0
	for i in range(5):
		camp1 += (data['players'][i]['camps_stacked'])
	for i in range(10):
		camp2 += (data['players'][i]['camps_stacked'])
	camp2 = camp2 - camp1
	return (camp1,camp2)

def neutralfarmed(match_id):
	s = 'https://api.opendota.com/api/matches/' + str(match_id)
	r = requests.get(s) #send request GET to opendota
	if r.status_code == 200:
		data = r.json()
	result = []
	for i in range(10):
		result.append([data['players'][i]['neutral_kills'],data['players'][i]['name']])
	return result

def lanefarmed(match_id):
	s = 'https://api.opendota.com/api/matches/' + str(match_id)
	r = requests.get(s) #send request GET to opendota
	if r.status_code == 200:
		data = r.json()
	result = []
	for i in range(10):
		result.append([data['players'][i]['lane_kills'],data['players'][i]['name']])
	return result

def ancientfarmed(match_id):
	s = 'https://api.opendota.com/api/matches/' + str(match_id)
	r = requests.get(s) #send request GET to opendota
	if r.status_code == 200:
		data = r.json()
	result = []
	for i in range(10):
		result.append([data['players'][i]['ancient_kills'],data['players'][i]['name']])
	return result

def lasthit(match_id):
	s = 'https://api.opendota.com/api/matches/' + str(match_id)
	r = requests.get(s) #send request GET to opendota
	if r.status_code == 200:
		data = r.json()
	result = []
	for i in range(10):
		result.append([data['players'][i]['last_hits'],data['players'][i]['name']])
	return result

def denies(match_id):
	s = 'https://api.opendota.com/api/matches/' + str(match_id)
	r = requests.get(s) #send request GET to opendota
	if r.status_code == 200:
		data = r.json()
	result = []
	for i in range(10):
		result.append([data['players'][i]['denies'],data['players'][i]['name']])
	return result

def deward_obs(match_id):
	s = 'https://api.opendota.com/api/matches/' + str(match_id)
	r = requests.get(s) #send request GET to opendota
	if r.status_code == 200:
		data = r.json()
	dw1 = 0
	dw2 = 0
	for i in range(5):
		dw1 += (data['players'][i]['observer_kills'])
	for i in range(10):
		dw2 += (data['players'][i]['observer_kills'])
	dw2 = dw2 - dw1
	return (dw1,dw2)


def banpick(match_id):
	s = 'https://api.opendota.com/api/matches/' + str(match_id)
	r = requests.get(s) #send request GET to opendota
	if r.status_code == 200:
		data = r.json()
	return data['picks_bans'] # need to reformat
