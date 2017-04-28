import numpy as np
import matchparsing

match_id = [3142390443, 3144097046, 3144175535, 3142994571]

def support_combo_score():
	#we scrape the lineup and evaluate base on three categories: greedy, defensive, aggressive
	#we may appy statistical learning models in this problem

	pass

def team_pick():
	#fix team id, scrape the data
	pass

def team_ban_pick():
	#mostly concerns with ban/pick order, also ban/pick priority like first ban, first pick, last pick
	pass

def player_pick(player):
	pass

def pro_match(id):
	pass

def objectives(): #includes roshan, towers, shrines and timing
	pass

def duration():
	pass

def firstbloodtime(match_id):
	s = 0
	for i in range(len(match_id)):
		s += matchparsing.first_blood(match_id[i])
	return s

print firstbloodtime(match_id = match_id)
