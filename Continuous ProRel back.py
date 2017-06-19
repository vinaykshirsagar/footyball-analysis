

#Dictionaries associates team with the year of changed league and point tally in that league.
#There is a dictionary for promoted teams and a dictionary for relegated teams.

#Code intended for promotion and relegation from first league

from parse_text import Data

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
			thisYear.add(Data[year][1][pos]["name"])
	promoted = thisYear - lastYear
	relegated = lastYear - thisYear
	for team in promoted:
		if team in toBePromoted:
			returnTime = yearCount - toBePromoted[team]["Year"]
			print("Return time: ", surviveTime)
			if returnTime == 1:
				returnedInOneYearCount += 1
			if returnTime <= 3:
				returnedInThreeYearCount += 1
			if returnTime <= 5:
				returnedInFiveYearCount += 1
			if returnTime <= 10:
				returnedInTenYearCount += 1
			toBePromoted.pop(team)
			riseCount += 1
			
		#add team to toBeRelegated
		
		toBeRelegated[team] = {}
		toBeRelegated[team]["Year"] = yearCount
		print(team, "was promoted in ", yearCount)
		#toBeRelegated[team]["Points"] = #more code will be needed to get the points, figure this out once the other stuff works
	for team in relegated:
		if team in toBeRelegated:
			surviveTime = yearCount - toBeRelegated[team]["Year"]
			print("Survivetime: ", surviveTime)
			if surviveTime >= 10:
				survivedTenYearCount += 1
			if surviveTime >= 5:
				survivedFiveYearCount += 1
			if surviveTime >= 3:
				survivedThreeYearCount += 1
			if surviveTime > 1:
				survivedOneYearCount += 1
				print("Survived one year")
				
			toBeRelegated.pop(team)
			dropCount += 1
		
		toBePromoted[team] = {}
		toBePromoted[team]["Year"] = yearCount
		print(team, "was relegated in ", yearCount)
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