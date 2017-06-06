import pickle
from parse_text import Data
from epl_table_simulation import SimTeam
from math import sqrt
import numpy as np

with open('sim_data.pkl', 'rb') as simfile:
	Sim_Data = pickle.load(simfile)

def calc_our_metric(sim_league, act_league):
	x = 0
	for i in range(len(sim_league)):
		x += (sim_league[i].points - act_league[i+1]['points'])**2
	return sqrt(x/len(sim_league))

def fill_data():
	Var_Data = {}
	for year in Data.keys():
		Var_Data[year] = year_dict = {}
		for league in Data[year].keys():
			sim_league = Sim_Data[year][league]
			act_league = Data[year][league]
			league_dict = {}
			league_dict['our metric'] = calc_our_metric(sim_league, act_league)
			league_dict['sim table SD'] = np.std([team.points for team in Sim_Data[year][league]])
			act_table = Data[year][league]
			league_dict['act table SD'] = np.std([act_table[pos]['points'] for pos in act_table.keys() if pos not in ['away goals', 'home goals']])
			year_dict[league] = league_dict
	return Var_Data

fill_data()