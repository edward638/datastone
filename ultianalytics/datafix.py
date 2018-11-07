#written by Junmo - Python v3.6
import csv
import warnings

warnings.simplefilter('always')

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

def read_in_file(filename):
	#print filename
	print("scraping file: " + filename)

	#initialize return variables
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
		games = 0
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
				pass

			#logic for game over
			elif (row[7] == 'Cessation') and (row[8] == 'GameOver'):
				#edit return variables
				for g_record, t_record in zip(game_records, total_records):
					for player in g_record:
						add_to_total_record(player, t_record)
						t_record[player].append(g_record[player])
				
				#reset local variables
				games += 1
				for record in game_records:
					record.clear()

			#logic for offense
			elif row[7] == 'Offense':
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

			#increment row count
			row_count += 1

		#print number of games
		print("number of games: ", games)

	#return variables
	return total_records

records = read_in_file('RaleighFlyers2018-stats.csv')