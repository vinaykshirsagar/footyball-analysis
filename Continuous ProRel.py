



#Dictionaries associates team with the year of changed league and point tally in that league.
#There is a dictionary for promoted teams and a dictionary for relegated teams.

#Code intended for promotion and relegation from first league

from parse_text import Data


#looks up to see if this team name has an alias and returns the team name to proceed with
#it would be more efficient to change the csv/txt files themselves or to change the parsing
#code but this is quick fix to test this code


def checkAlt(name):
	if name not in alternates:
		return name
	else:
		return alternates[name]
	

#This dictionary is probably complete but there is a chance I could have missed some
alternates = {'Man United': 'Manchester United', 'Man City': 'Manchester City', 'Norwich': 'Norwich City', 
     'Sheffield Weds': 'Sheffield Wednesday', 'Nott\'m Forest': 'Nottingham Forest', 'QPR': 'Queens Park Rangers',
     'Leeds': 'Leeds United', 'Tottenham': 'Tottenham Hotspur', 'Oldham': 'Oldham Athletic', 'Blackburn': 'Blackburn Rovers',
     'Coventry': 'Coventry City', 'Ipswich': 'Ipswich Town', 'Newcastle United': 'Newcastle', 'Wolves': 'Wolverhampton Wanderers',
     'Tranmere': 'Tranmere Rovers', 'Leicester': 'Leicester City', 'Derby': 'Derby County', 'Stoke': 'Stoke City',
     'Charlton': 'Charlton Athletic', 'Grimsby': 'Grimsby Town', 'Peterboro': 'Peterborough United',
     'Bolton': 'Bolton Wanderers', 'Southend': 'Southend United', 'Luton Town': 'Luton Town',
     'West Brom': 'West Bromwich Albion', 'Birmingham': 'Birmingham City', 'Oxford': 'Oxford United',
     'Plymouth': 'Plymouth Argyle', 'Stockport': 'Stockport County', 'Bradford': 'Bradford City',
     'Hull': 'Hull City', 'Bristol Rvs': 'Bristol Rovers', 'Cambridge': 'Cambridge United',
     'Huddersfield': 'Huddersfield Town', 'Swansea': 'Swansea City', 'Brighton': 'Brighton & Hove Albion',
     'Rotherham': 'Rotherham United', 'Bournemouth': 'AFC Bournemouth', 'Exeter': 'Exeter City',
     'Hartlepool': 'Hartlepool United', 'Preston': 'Preston North End', 'Mansfield': 'Mansfield Town',
     'Wigan': 'Wigan Athletic'
}

years = sorted(list(Data.keys()))

toBePromoted = {}
toBeRelegated = {} 
#teamsEncountered = {}

returnedInOneYearCount = 0
returnedInThreeYearCount = 0
returnedInFiveYearCount = 0
returnedInTenYearCount = 0
riseCount = 0 #total number of promoted teams (for fraction)

survivedOneYearCount = 0
survivedThreeYearCount = 0
survivedFiveYearCount = 0
survivedTenYearCount = 0
dropCount = 0;

yearCount = 0; #this count ensures that we don't count years without seasons in the survivorship or return tallies

lastYear = set() #who was in the prem last year (initially empty)
for year in years:
	print("\tYear: ", year)
	#if(len(lastYear) == 0): #if this the first year we don't have any promotion/relegation info to compare against
	thisYear = set()
	for pos in Data[year][1]:
		if pos not in ['home goals', 'away goals']:
			''' this code is likley unnecessary
			if Data[year][1][pos]["name"] not in teamsEncountered:
				toBeRelegated[Data[year][1][pos]["name"]] = {}
				#The year this team was promoted (here they were a team to start in the highest division)
				toBeRelegated[Data[year][1][pos]["name"]]["Year"] = yearCount
				#The point tally of this team the year it was promoted (-1 to indicate they started in the first division)
				toBeRelegated[Data[year][1][pos]["name"]]["Points"] = -1
				teamsEcountered.append(Data[year][1][pos]["name"])
			'''
			thisYear.add(checkAlt(Data[year][1][pos]["name"]))
	promoted = thisYear - lastYear
	relegated = lastYear - thisYear
	for team in promoted:
		if checkAlt(team) in toBePromoted:
			returnTime = yearCount - toBePromoted[checkAlt(team)]["Year"]
			print("\nReturn time: ", surviveTime)
			if returnTime == 1:
				returnedInOneYearCount += 1
			if returnTime <= 3:
				returnedInThreeYearCount += 1
			if returnTime <= 5:
				returnedInFiveYearCount += 1
			if returnTime <= 10:
				returnedInTenYearCount += 1
			toBePromoted.pop(checkAlt(team))
			riseCount += 1
			
		#add team to toBeRelegated
		
		toBeRelegated[checkAlt(team)] = {}
		toBeRelegated[checkAlt(team)]["Year"] = yearCount
		print(team, "was promoted in ", yearCount)
		#toBeRelegated[team]["Points"] = #more code will be needed to get the points, figure this out once the other stuff works
	for team in relegated:
		if checkAlt(team) in toBeRelegated:
			surviveTime = yearCount - toBeRelegated[checkAlt(team)]["Year"]
			print("\nSurvivetime: ", surviveTime)
			if surviveTime >= 10:
				survivedTenYearCount += 1
			if surviveTime >= 5:
				survivedFiveYearCount += 1
			if surviveTime >= 3:
				survivedThreeYearCount += 1
			if surviveTime > 1:
				survivedOneYearCount += 1
				
			toBeRelegated.pop(checkAlt(team))
			dropCount += 1
		
		toBePromoted[checkAlt(team)] = {}
		toBePromoted[checkAlt(team)]["Year"] = yearCount
		print(checkAlt(team), "was relegated in ", yearCount)
	lastYear = thisYear
	
	yearCount += 1

print("Fraction of teams to survive at least")
print("\tOne year: {:.10f}".format(survivedOneYearCount/ float(dropCount)))
print("\tThree years: {:.10f}".format(survivedThreeYearCount/ float(dropCount)))
print("\tFive years: {:f}".format(survivedFiveYearCount/ float(dropCount)))
print("\tTen years: {:f}".format(survivedTenYearCount/ float(dropCount)))

print("Fraction of teams to return in at most")
print("\tOne year: {:f}".format(returnedInOneYearCount/ float(riseCount)))
print("\tThree years: {:f}".format(returnedInThreeYearCount/ float(riseCount)))
print("\tFive years: {:f}".format(returnedInFiveYearCount/ float(riseCount)))
print("\tTen years: {:f}".format(returnedInTenYearCount/ float(riseCount)))

#when team changes league, increase the appropriate counters representing how long they stayed in the league
#, increment the counter showing that they are team that changed league (to take find the percentage of teams)
# that stayed 1, 3, 5, 10 years
# add point tally to likeliness-to-change-league analysis later