CREATE TABLE Temporary
(Player VARCHAR(256) NOT NULL PRIMARY KEY, 
 Goals DECIMAL(3,0) NOT NULL CHECK (Goals >= 0),
 Assists DECIMAL(3,0) NOT NULL CHECK (Assists >= 0), 
 Blocks DECIMAL(3,0) NOT NULL CHECK (Blocks >= 0), 
 Catches DECIMAL(3,0) NOT NULL CHECK (Catches >= 0), 
 Completions DECIMAL(3,0) NOT NULL CHECK (Completions >= 0),
 Throwaways DECIMAL(3,0) NOT NULL CHECK (Throwaways >= 0),
 Drops DECIMAL(3,0) NOT NULL CHECK (Drops >= 0), 
 Callahans DECIMAL(3,0) NOT NULL CHECK (Callahans >= 0));

FOR wk IN 1..17
	COPY Temporary
	FROM format('/../data/polleddata/wk%s_AUDL_2018.csv', wk) DELIMITER ',' CSV HEADER;

	INSERT INTO PlayerPerformance
	SELECT wk, *
	FROM Temporary;

	TRUNCATE TABLE Temporary;
END LOOP;