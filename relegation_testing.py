from parse_text import Data

years = sorted(list(Data.keys()))
ex_year = '2010-11'
ex_year_dict = Data[ex_year][1]
ex_year_teams = set([ex_year_dict[pos]['name'] for pos in ex_year_dict.keys() if pos not in ['home goals', 'away goals']])
ex_year = '2011-12'
ex_year_dict = Data[ex_year][1]
ex_year2_teams = set([ex_year_dict[pos]['name'] for pos in ex_year_dict.keys() if pos not in ['home goals', 'away goals']])

#print("Teams relegated in {0}: {1}".format(ex_year, ex_year_teams-ex_year2_teams))
#print("Teams promoted in {0}: {1}".format(ex_year, ex_year2_teams-ex_year_teams))
#Only 1st league!
relegated = {}
promoted = {}
for year in years:
	year_num = int(year[:4])
	next_year_num = year_num+1
	next_year = str(next_year_num) + '-' + str(next_year_num%100 + 1)
	if next_year not in years:
		continue
	stuff = []
	for y in [year, next_year]:
		y_dict = Data[y][1]
		stuff.append(set([y_dict[pos]['name'] for pos in y_dict.keys() if pos not in ['home goals', 'away goals']]))
	relegated[year] = list(stuff[0]-stuff[1])
	promoted[year]  = list(stuff[1]-stuff[0])
	print("Teams relegated after {0} season: {1}".format(year, relegated[year]))
	print("Teams promoted after {0} season: {1}\n".format(year, promoted[year]))