#written by Junmo - Python v3.6
import sys
import csv
import os
import warnings
from scipy.stats import poisson

#read a file
def simple_read(filename):
	#print filename
	print("READING FILE: " + filename)

	#open file
	rows = []
	with open(filename, newline='') as file:
		reader = csv.reader(file, delimiter=',')
		row_count = 0
		for row in reader:
			if row_count == 0:
				row_count += 1
				continue
			else:
				rows.append(row)
	return rows

#poll from poisson with average from values read in
def poll_poisson():
	#initialize polled rows
	polled_rows = []
	header = ["player", "goals", "assists", "blocks", "catches", "completions", "throwaways", "drops", "callahans"]
	polled_rows.append(header)

	#read in data
	rows = simple_read(os.path.join('fixeddata', 'AUDL_2018.csv'))
	for row in rows:
		#generate polled row
		player = row[0]
		goals = poisson.rvs(float(row[1]))
		assists = poisson.rvs(float(row[2]))
		blocks = poisson.rvs(float(row[3]))
		catches = poisson.rvs(float(row[4]))
		completions = poisson.rvs(float(row[5]))
		throwaways = poisson.rvs(float(row[6]))
		drops = poisson.rvs(float(row[7]))
		callahans = poisson.rvs(float(row[8]))
		polled_rows.append([player, goals, assists, blocks, catches, completions, throwaways, drops, callahans])

	#return polled rows
	return polled_rows

#write a file
def simple_write(filename, rows):
	#print filename
	print("WRITING FILE: " + filename)

	#open file
	with open(filename, 'w', newline='') as file:
		writer = csv.writer(file)
		writer.writerows(rows)

#week from command line args
week = 0
try:
	week = int(sys.argv[1])
	if week <= 0:
		week = 0
		warnings.warn("invalid week; writing values to week 0")
except:
	warnings.warn("invalid week; writing values to week 0")

#main statments
polled_rows = poll_poisson()
simple_write(os.path.join('polleddata', 'wk' + str(week) + '_AUDL_2018.csv'), polled_rows)