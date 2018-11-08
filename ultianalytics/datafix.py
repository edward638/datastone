#written by Junmo - Python v3.6
import csv
import os
import warnings

#helper functions
def add_to_total_record(player, record):
	if player not in record:
		record[player] = []

def add_to_game_record(player, record):
	if player not in record:
		record[player] = 0

def print_records(records):
	for i,record in enumerate(records):
		print("----------record", i)
		for player in record:
			print(player, record[player])

#read an AUDL data file
#returns : (number of games, list of data in dictionaries)
#data order : goals, assists, blocks, catches, completions, throwaways, drops, callahans
def read_AUDL_file(filename, debug = False):
	#print filename
	print("READING FILE: " + filename)

	#toggle suppress
	if debug:
		warnings.simplefilter('always')
	else:
		warnings.simplefilter('ignore')

	#initialize return variables
	games = 0
	total_goals = {}
	total_assists = {}
	total_blocks = {}
	total_catches = {}
	total_completions = {}
	total_throwaways = {}
	total_drops = {}
	total_callahans = {}
	total_records = [total_goals, total_assists, total_blocks, total_catches, total_completions, total_throwaways, total_drops, total_callahans]

	#open file
	with open(filename, newline='') as file:
		reader = csv.reader(file, delimiter=',')
		row_count = 1

		#initialize local variables
		date = ""
		game_goals = {}
		game_assists = {}
		game_blocks = {}
		game_catches = {}
		game_completions = {}
		game_throwaways = {}
		game_drops = {}
		game_callahans = {}
		game_records = [game_goals, game_assists, game_blocks, game_catches, game_completions, game_throwaways, game_drops, game_callahans]
		
		#loop through rows
		for row in reader:
			#skip header row
			if row_count == 1:
				row_count += 1
				continue

			#logic for new game
			if row[0] != date:
				#edit return variables
				for g_record, t_record in zip(game_records, total_records):
					for player in g_record:
						add_to_total_record(player, t_record)
						t_record[player].append(g_record[player])
				games += 1

				#reset local variables
				date = row[0]
				for record in game_records:
					record.clear()

			#logic for offense
			if row[7] == 'Offense':
				#offense:(played)
				for i in range(13,41):
					#check if real player
					if row[i] != "":
						#then add to game_records
						player = row[i]
						for record in game_records:
							add_to_game_record(player, record)

				#offense:(goals, assists)
				if row[8] == 'Goal':
					passer = row[9]
					receiver = row[10]

					#increment goal
					if receiver not in game_goals:
						warnings.warn("receiver not in game_goals. row: " + str(row_count))
					else:
						game_goals[receiver] += 1
					#also increment catch
					if receiver not in game_catches:
						warnings.warn("receiver not in game_catches. row: " + str(row_count))
					else:
						game_catches[receiver] += 1

					#increment assist
					if passer not in game_assists:
						warnings.warn("passer not in game_assists. row: " + str(row_count))
					else:
						game_assists[passer] += 1
					#also increment completion
					if passer not in game_completions:
						warnings.warn("passer not in game_completions. row: " + str(row_count))
					else:
						game_completions[passer] += 1

				#offense:(catches, completions)
				elif row[8] == 'Catch':
					passer = row[9]
					receiver = row[10]

					#increment catch
					if receiver not in game_catches:
						warnings.warn("receiver not in game_catches. row: " + str(row_count))
					else:
						game_catches[receiver] += 1

					#increment completion
					if passer not in game_completions:
						warnings.warn("passer not in game_completions. row: " + str(row_count))
					else:
						game_completions[passer] += 1

				#offense:(throwaways)
				elif row[8] == 'Throwaway':
					passer = row[9]

					#increment throwaway
					if passer not in game_throwaways:
						warnings.warn("passer not in game_throwaways. row: " + str(row_count))
					else:
						game_throwaways[passer] += 1

				#offense:(drops)
				elif row[8] == 'Drop':
					receiver = row[10]

					#increment drop
					if receiver not in game_drops:
						warnings.warn("receiver not in game_drops. row: " + str(row_count))
					else:
						game_drops[receiver] += 1

			#logic for defense
			elif row[7] == 'Defense':
				#defense:(played)
				for i in range(13,41):
					#check if real player
					if row[i] != "":
						#then add to game_records
						player = row[i]
						for record in game_records:
							add_to_game_record(player, record)

				#defense:(blocks)
				if row[8] == 'D':
					defender = row[11]

					#increment block
					if defender not in game_blocks:
						warnings.warn("defender not in game_blocks. row: " + str(row_count))
					else:
						game_blocks[defender] += 1

				#defense:(callahans)
				if row[8] == 'Callahan':
					defender = row[11]

					#increment callahan
					if defender not in game_callahans:
						warnings.warn("defender not in game_callahans. row: " + str(row_count))
					else:
						game_callahans[defender] += 1
					#also increment block
					if defender not in game_blocks:
						warnings.warn("defender not in game_blocks. row: " + str(row_count))
					else:
						game_blocks[defender] += 1
					#also increment goal
					if defender not in game_goals:
						warnings.warn("defender not in game_goals. row: " + str(row_count))
					else:
						game_goals[defender] += 1
					#also increment catch
					if defender not in game_catches:
						warnings.warn("defender not in game_catches. row: " + str(row_count))
					else:
						game_catches[defender] += 1

			#increment row count
			row_count += 1

		#after loop : edit return variables
		for g_record, t_record in zip(game_records, total_records):
					for player in g_record:
						add_to_total_record(player, t_record)
						t_record[player].append(g_record[player])

	#return variables
	return games, total_records

#datafix logic
def fix_raw_data(directory):
	#initialize rows
	rows = []
	header = ["player", "goals", "assists", "blocks", "catches", "completions", "throwaways", "drops", "callahans"]
	rows.append(header)
	for filename in os.listdir(directory):
		#read in data
		games, records = read_AUDL_file(os.path.join(directory, filename))

		#generate row
		players = sorted(records[0])
		for player in players:
			row = [player, sum(records[0][player])/games, sum(records[1][player])/games,
				sum(records[2][player])/games, sum(records[3][player])/games,
				sum(records[4][player])/games, sum(records[5][player])/games,
				sum(records[6][player])/games, sum(records[7][player])/games]
			rows.append(row)

	#return rows
	return rows

#write a file
def simple_write(filename, rows):
	#print filename
	print("WRITING FILE: " + filename)

	#open file
	with open(filename, 'w', newline='') as file:
		writer = csv.writer(file)
		writer.writerows(rows)

#main statements
rows = fix_raw_data('rawdata')
simple_write(os.path.join('fixeddata', 'AUDL_2018.csv'), rows)