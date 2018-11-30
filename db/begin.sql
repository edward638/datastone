-- PlayerStatus table (Eddie makes this in Flask, no need to use this CREATE TABLE statement)
CREATE TABLE PlayerStatus
(player_id DECIMAL(4,0) NOT NULL REFERENCES PlayerData.id PRIMARY KEY,
 name VARCHAR(256) NOT NULL REFERENCES PlayerData.name,
 score_avg DECIMAL(4,9), NOT NULL,
 score_sd DECIMAL(4,9) NOT NULL,
 user_id DECIMAL(2,0),   
 active DECIMAL(1,0) NOT NULL CHECK (Active = 1 OR Active = 0));

-- SQL statement to populate the PlayerStatus table
WITH IND(i) AS (SELECT * FROM generate_series(0, (SELECT COUNT(*) FROM PlayerData) - 1), 1))
INSERT INTO PlayerStatus
	(i,
	 SELECT name FROM PlayerData WHERE id = i,
	 SELECT (12*goals_avg+12*assists_avg+24*blocks_avg+0.5*catches_avg+0.5*completions_avg-14*throwaways_avg-14*drops_avg+72*callahans_avg) FROM PlayerData WHERE id = i,
	 SELECT (SQRT((12*goals_sd)^2+(12*assists_sd)^2+(24*blocks_sd)^2+(0.5*catches_sd)^2+(0.5*completions_sd)^2+(-14*throwaways_sd)^2+(-14*drops_sd)^2)+(72*callahans_sd)^2) FROM PlayerData WHERE id = i,
	 -1,
	 0)
FROM IND; 

-- PlayerWeeklyStats table (Eddie makes this in Flask, no need to use this CREATE TABLE statement)
CREATE TABLE PlayerWeeklyStats
(player_id DECIMAL(4,0) NOT NULL REFERENCES PlayerData.id,
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
WITH INDI(i) AS (SELECT * FROM generate_series(0, (SELECT COUNT(*) FROM PlayerStatus) - 1), 1))
	WITH INDJ(j) AS (SELECT * FROM generate_series(1, 16, 1))
		INSERT INTO PlayerWeeklyStats 
			(i,
			 j,
			 SELECT (MAX(ROUND(goals_avg+goals_sd*(SQRT(-2*LOG(RAND()))*COS(2*PI()*RAND()))),0)) FROM PlayerData WHERE id = i,
			 SELECT (MAX(ROUND(assists_avg+assists_sd*(SQRT(-2*LOG(RAND()))*COS(2*PI()*RAND()))),0)) FROM PlayerData WHERE id = i,
			 SELECT (MAX(ROUND(blocks_avg+blocks_sd*(SQRT(-2*LOG(RAND()))*COS(2*PI()*RAND()))),0)) FROM PlayerData WHERE id = i,
			 SELECT (MAX(ROUND(catches_avg+catches_sd*(SQRT(-2*LOG(RAND()))*COS(2*PI()*RAND()))),0)) FROM PlayerData WHERE id = i,
			 SELECT (MAX(ROUND(completions_avg+completions*(SQRT(-2*LOG(RAND()))*COS(2*PI()*RAND()))),0)) FROM PlayerData WHERE id = i,
			 SELECT (MAX(ROUND(throwaways_avg+throwaways_sd*(SQRT(-2*LOG(RAND()))*COS(2*PI()*RAND()))),0)) FROM PlayerData WHERE id = i,
			 SELECT (MAX(ROUND(drops_avg+drops_sd*(SQRT(-2*LOG(RAND()))*COS(2*PI()*RAND()))),0)) FROM PlayerData WHERE id = i,
			 SELECT (MAX(ROUND(callahans_avg+callahans_sd*(SQRT(-2*LOG(RAND()))*COS(2*PI()*RAND()))),0)) FROM PlayerData WHERE id = i,
			 0)
	FROM INDI;
FROM INDJ;

-- SQL statement to populate scores in PlayerWeeklyStats
WITH INDI(i) AS (SELECT * FROM generate_series(0, (SELECT COUNT(*) FROM PlayerStatus) - 1), 1))
	WITH INDJ(j) AS (SELECT * FROM generate_series(1, 16, 1))
			(UPDATE PlayerWeeklyStats 
			SET score = (12*goals+12*assists+24*blocks+0.5*catches+0.5*completions-14*throwaways-14*drops+72*callahans)
			WHERE player_id = i AND week = j)
	FROM INDI;
FROM INDJ;

