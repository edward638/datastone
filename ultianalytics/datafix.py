import csv

def scrape_file(filename):
	goals_year = {}
	with open(filename) as file:
		reader = csv.reader(file)
		row_count = 0

		date_time = ""
		week = 0
		goals_week = {}
		
		for row in reader:
			if row_count == 0:
				continue

			if row[0] != date_time:
				for key in goals_week:
					if key not in goals_year:
						goals_year[key] = []
					goals_year[key].append(goals_week[key])
					goals_week[key] = 0
				week += 1
				date_time = row[0]

			if row[8] == "Goal":
				passer = row[9]
				receiver = row[10]
				if receiver not in goals_week:
					goals_week[receiver] = 0
				goals_week[receiver] += 1

			row_count += 1

	return goals_year

print(scrape_file('RaleighFlyers2018-stats.csv'))