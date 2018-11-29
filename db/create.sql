CREATE TABLE Players
(PlayerID INTEGER NOT NULL PRIMARY KEY,
 GoalsAvg REAL NOT NULL CHECK (GoalsAvg >= 0),
 AssistsAvg REAL NOT NULL CHECK (AssistsAvg >= 0),
 BlocksAvg REAL NOT NULL CHECK (BlocksAvg >= 0)
 CatchesAvg REAL NOT NULL CHECK (CatchesAvg >= 0),
 CompletionsAvg REAL NOT NULL CHECK (CompletionsAvg >= 0),
 ThrowawaysAvg REAL NOT NULL CHECK (ThrowawaysAvg >= 0),
 DropsAvg REAL NOT NULL CHECK (DropsAvg >= 0),
 CallahansAvg REAL NOT NULL CHECK (CallahansAvg >= 0),
 Taken CHAR(1) NOT NULL CHECK (Taken = 'Y' or Taken = 'N'));

CREATE TABLE PlayerPerformance
(Week DECIMAL(2,0) NOT NULL CHECK (Week >= 1 and Week <= 17),
 PlayerID INTEGER NOT NULL REFERENCES Players(PlayerID),
 Goals DECIMAL(3,0) NOT NULL CHECK (Goals >= 0),
 Assists DECIMAL(3,0) NOT NULL CHECK (Assists >= 0),
 Blocks DECIMAL(3,0) NOT NULL CHECK (Blocks >= 0),
 Catches DECIMAL(3,0) NOT NULL CHECK (Catches >= 0),
 Completions DECIMAL(3,0) NOT NULL CHECK (Completions >= 0),
 Throwaways DECIMAL(3,0) NOT NULL CHECK (Throwaways >= 0),
 Drops DECIMAL(3,0) NOT NULL CHECK (Drops >= 0),
 Callahans DECIMAL(3,0) NOT NULL CHECK (Callahans >= 0),
 PRIMARY KEY(Week, Player));

CREATE TABLE Users
(UserID DECIMAL(2,0) NOT NULL PRIMARY KEY,
 TeamName VARCHAR(256) NOT NULL);

CREATE TABLE Rosters
(UserID INTEGER NOT NULL REFERENCES Users(UserID) PRIMARY KEY,
 PlayerID INTEGER NOT NULL REFERENCES Players(PlayerID),
 Active CHAR(1) NOT NULL CHECK (Active = 'Y' or Active = 'N'));

CREATE TABLE WeeklyScores
(Week DECIMAL(2,0) NOT NULL CHECK (Week >= 1 and Week <= 17),
 UserID INTEGER NOT NULL REFERENCES Users(UserID),
 TeamScore REAL NOT NULL,
 PRIMARY KEY(Week, UserID));
