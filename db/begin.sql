-- player_status table (Eddie makes this in Flask, no need to use this CREATE TABLE statement)
CREATE TABLE player_status
(player_id DECIMAL(4,0) NOT NULL REFERENCES player_data.id PRIMARY KEY,
 name VARCHAR(256) NOT NULL REFERENCES player_data.name,
 score_avg DECIMAL(4,9), NOT NULL,
 score_sd DECIMAL(4,9) NOT NULL,
 user_id DECIMAL(2,0),   
 active DECIMAL(1,0) NOT NULL CHECK (Active = 1 OR Active = 0));

-- SQL statement to populate the player_status table
WITH IND(i) AS (SELECT * FROM generate_series(0, (SELECT COUNT(*) FROM player_data) - 1, 1))
INSERT INTO player_status SELECT
   i,
    (SELECT name FROM player_data WHERE id = i),
    (SELECT (12*goals_avg+12*assists_avg+24*blocks_avg+0.5*catches_avg+0.5*completions_avg-14*throwaways_avg-14*drops_avg+72*callahans_avg) FROM player_data WHERE id = i),
    (SELECT (SQRT((12*goals_sd)^2+(12*assists_sd)^2+(24*blocks_sd)^2+(0.5*catches_sd)^2+(0.5*completions_sd)^2+(-14*throwaways_sd)^2+(-14*drops_sd)^2)+(72*callahans_sd)^2) FROM player_data WHERE id = i),
    -1,
    0
FROM IND;

-- PlayerWeeklyStats table (Eddie makes this in Flask, no need to use this CREATE TABLE statement)
CREATE TABLE PlayerWeeklyStats
(player_id DECIMAL(4,0) NOT NULL REFERENCES player_data.id,
 week DECIMAL(2,0) NOT NULL CHECK (week >= 1 and week <= 16),
 goals DECIMAL(2,0) NOT NULL CHECK (goals >= 0),
 assists DECIMAL(2,0) NOT NULL CHECK (assists >= 0), 
 blocks DECIMAL(2,0) NOT NULL CHECK (blocks >= 0), 
 catches DECIMAL(3,0) NOT NULL CHECK (catches >= 0), 
 completions DECIMAL(3,0) NOT NULL CHECK (completions >= 0),
 throwaways DECIMAL(2,0) NOT NULL CHECK (throwaways >= 0),
 drops DECIMAL(2,0) NOT NULL CHECK (drops >= 0), 
 callahans DECIMAL(2,0) NOT NULL CHECK (callahans >= 0), 
 score DECIMAL(4,2), NOT NULL,
 PRIMARY KEY(player_id, week));

-- SQL statement to populate PlayerWeeklyStats with everything but score
-- RUN this big query, replacing the 1 on line 41 with 2, 3, ..., 16.
WITH IND(i) AS (SELECT * FROM generate_series(0, (SELECT COUNT(*) FROM player_status) - 1, 1))
		INSERT INTO player_weekly_stats SELECT
			i,
			 1,
			 (SELECT (ROUND(goals_avg+goals_sd*(SQRT(-2*LN(RANDOM()))*COS(2*PI()*RANDOM())))) FROM player_data WHERE id = i),
			 (SELECT (ROUND(assists_avg+assists_sd*(SQRT(-2*LN(RANDOM()))*COS(2*PI()*RANDOM())))) FROM player_data WHERE id = i),
			 (SELECT (ROUND(blocks_avg+blocks_sd*(SQRT(-2*LN(RANDOM()))*COS(2*PI()*RANDOM())))) FROM player_data WHERE id = i),
			 (SELECT (ROUND(catches_avg+catches_sd*(SQRT(-2*LN(RANDOM()))*COS(2*PI()*RANDOM())))) FROM player_data WHERE id = i),
			 (SELECT (ROUND(completions_avg+completions_sd*(SQRT(-2*LN(RANDOM()))*COS(2*PI()*RANDOM())))) FROM player_data WHERE id = i),
			 (SELECT (ROUND(throwaways_avg+throwaways_sd*(SQRT(-2*LN(RANDOM()))*COS(2*PI()*RANDOM())))) FROM player_data WHERE id = i),
			 (SELECT (ROUND(drops_avg+drops_sd*(SQRT(-2*LN(RANDOM()))*COS(2*PI()*RANDOM())))) FROM player_data WHERE id = i),
			 (SELECT (ROUND(callahans_avg+callahans_sd*(SQRT(-2*LN(RANDOM()))*COS(2*PI()*RANDOM())))) FROM player_data WHERE id = i),
			 0
FROM IND;

UPDATE player_weekly_stats
SET goals = 0
WHERE goals < 0;

UPDATE player_weekly_stats
SET assists = 0
WHERE assists < 0;

UPDATE player_weekly_stats
SET blocks = 0
WHERE blocks < 0;

UPDATE player_weekly_stats
SET catches = 0
WHERE catches < 0;

UPDATE player_weekly_stats
SET completions = 0
WHERE completions < 0;

UPDATE player_weekly_stats
SET drops = 0
WHERE drops < 0;

UPDATE player_weekly_stats
SET throwaways = 0
WHERE throwaways < 0;

UPDATE player_weekly_stats
SET callahans = 0
WHERE callahans < 0;

-- SQL statement to populate scores in PlayerWeeklyStats
update player_weekly_stats as t set
    score = (12*t.goals+12*t.assists+24*t.blocks+0.5*t.catches+0.5*t.completions-14*t.throwaways-14*t.drops+72*t.callahans)
from player_weekly_stats as c
where c.player_id = t.player_id;


