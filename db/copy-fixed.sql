CREATE TABLE Temporary
(Player VARCHAR(256) NOT NULL PRIMARY KEY,
 GoalsAvg REAL NOT NULL CHECK (GoalsAvg >= 0),
 AssistsAvg REAL NOT NULL CHECK (AssistsAvg >= 0), 
 BlocksAvg REAL NOT NULL CHECK (BlocksAvg >= 0)
 CatchesAvg REAL NOT NULL CHECK (CatchesAvg >= 0), 
 CompletionsAvg REAL NOT NULL CHECK (CompletionsAvg >= 0),
 ThrowawaysAvg REAL NOT NULL CHECK (ThrowawaysAvg >= 0),
 DropsAvg REAL NOT NULL CHECK (DropsAvg >= 0), 
 CallahansAvg REAL NOT NULL CHECK (CallahansAvg >= 0));

COPY Temporary
FROM '/data/fixeddata/AUDL_2018.csv' DELIMITER ',' CSV HEADER;

INSERT INTO Players
SELECT *, 'N'
FROM Temporary;

TRUNCATE TABLE Temporary;