
CREATE TABLE PlayerStatus
(player_id DECIMAL(4,0) NOT NULL REFERENCES PlayersData.PlayerID PRIMARY KEY,
 name VARCHAR(256) NOT NULL REFERENCES PlayersData.PlayerName,
 score_avg DECIMAL(4,9), NOT NULL,
 score_sd DECIMAL(4,9) NOT NULL,
 user_id DECIMAL(2,0),   
 active DECIMAL(1,0) NOT NULL CHECK (Active = 1 OR Active = 0));

--for each player with username 'X' with name 'Y' in the database

BEGIN 
	FOR i in 0 .. SELECT COUNT(*) FROM PlayerData
		INSERT INTO PlayerStatus 
		(i,
		 SELECT name FROM PlayerData WHERE player_id = i,
		 SELECT (12*goals_avg+12*assists_avg+24*blocks_avg+0.5*catches_avg+0.5*completions_avg-14*throwaways_avg-14*drops_avg+72*callahans_avg) FROM PlayerData WHERE PlayerData.id = i,
		 SELECT (SQRT((12*goals_sd)^2+(12*assists_sd)^2+(24*blocks_sd)^2+(0.5*catches_sd)^2+(0.5*completions_sd)^2+(-14*throwaways_sd)^2+(-14*drops_sd)^2)+(72*callahans_sd)^2) FROM PlayerData WHERE PlayerData.id = i,
		 -1,
		 0);
	END LOOP;
END;

CREATE TABLE PlayerWeeklyStats
(player_id DECIMAL(4,0) NOT NULL REFERENCES PlayersData.PlayerID,
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

BEGIN 
	FOR i in 0 .. SELECT COUNT(*) FROM PlayerStatus
		FOR j in 1 .. 16
			INSERT INTO PlayerScores 
			(i,
			 j,
			 SELECT (MAX(ROUND(goals_avg+goals_sd*(SQRT(-2*LOG(RAND()))*COS(2*PI()*RAND()))),0)) FROM PlayerData WHERE PlayerData.id = i,
			 SELECT (MAX(ROUND(assists_avg+assists_sd*(SQRT(-2*LOG(RAND()))*COS(2*PI()*RAND()))),0)) FROM PlayerData WHERE PlayerData.id = i,
			 SELECT (MAX(ROUND(blocks_avg+blocks_sd*(SQRT(-2*LOG(RAND()))*COS(2*PI()*RAND()))),0)) FROM PlayerData WHERE PlayerData.id = i,
			 SELECT (MAX(ROUND(catches_avg+catches_sd*(SQRT(-2*LOG(RAND()))*COS(2*PI()*RAND()))),0)) FROM PlayerData WHERE PlayerData.id = i,
			 SELECT (MAX(ROUND(completions_avg+completions*(SQRT(-2*LOG(RAND()))*COS(2*PI()*RAND()))),0)) FROM PlayerData WHERE PlayerData.id = i,
			 SELECT (MAX(ROUND(throwaways_avg+throwaways_sd*(SQRT(-2*LOG(RAND()))*COS(2*PI()*RAND()))),0)) FROM PlayerData WHERE PlayerData.id = i,
			 SELECT (MAX(ROUND(drops_avg+drops_sd*(SQRT(-2*LOG(RAND()))*COS(2*PI()*RAND()))),0)) FROM PlayerData WHERE PlayerData.id = i,
			 SELECT (MAX(ROUND(callahans_avg+callahans_sd*(SQRT(-2*LOG(RAND()))*COS(2*PI()*RAND()))),0)) FROM PlayerData WHERE PlayerData.id = i,
			 0);
		END LOOP;
	END LOOP;
END;

BEGIN 
	FOR i in 0 .. SELECT COUNT(*) FROM PlayerStatus
		FOR j in 1 .. 16
			UPDATE PlayerWeeklyStats 
			SET score = (12*goals+12*assists+24*blocks+0.5*catches+0.5*completions-14*throwaways-14*drops+72*callahans)
			WHERE PlayerWeeklyStats.player_id = i AND PlayerWeeklyStats.week = j;
		END LOOP;
	END LOOP;
END;

---------------------------------------

