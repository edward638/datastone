import csv

with open() as file:
	reader = csv.reader(file)
	row_count = 0
	time = ""
	week = 0
	goals_week = {}
	goals_year = {}
	for row in reader:
		if row_count == 0:
			continue
		if row[0] != time:
			for key in goals_week:
				goals_year[key].append(goals_week[key])
			week++
			time = row[0]


		row_count++