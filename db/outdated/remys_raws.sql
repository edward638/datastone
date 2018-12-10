CREATE TABLE Users
(UserID DECIMAL(2,0) NOT NULL PRIMARY KEY,
 TeamName VARCHAR(256) NOT NULL);

CREATE TABLE Players
(Player VARCHAR(256) NOT NULL PRIMARY KEY,
 GoalsAvg DECIMAL(2,0) NOT NULL CHECK (GoalsAvg >= 0),
 AssitsAvg DECIMAL(2,0) NOT NULL CHECK (AssistsAvg >= 0), 
 BlocksAvg DECIMAL(3,2) NOT NULL CHECK (BlocksAvg >= 0)
 CatchesAvg DECIMAL(3,0) NOT NULL CHECK (CatchesAvg >= 0), 
 CompletionsAvg DECIMAL(3,0) NOT NULL CHECK (CompletionsAvg >= 0),
 ThrowawaysAvg DECIMAL(2,0) NOT NULL CHECK (ThrowawaysAvg >= 0),
 DropsAvg DECIMAL(2,0) NOT NULL CHECK (DropsAvg >= 0), 
 CallahansAvg DECIMAL(2,0) NOT NULL CHECK (CallahansAvg >= 0),
 ScoreAvg DECIMAL(4,9), NOT NULL,
 ScoreVariance DECIMAL(4,9), NOT NULL CHECK (ScoreVariance >= 0)),
 Taken CHAR(1) NOT NULL CHECK (Taken = 'Y' or Taken = 'N'));

CREATE TABLE PlayerPerformance
(Week DECIMAL(2,0) NOT NULL CHECK (Week >= 1 and Week <= 17),
 Player VARCHAR(256) NOT NULL REFERENCES Players.Player, 
 Goals DECIMAL(2,0) NOT NULL CHECK (Goals >= 0),
 Assists DECIMAL(2,0) NOT NULL CHECK (Assists >= 0), 
 Blocks DECIMAL(2,0) NOT NULL CHECK (Blocks >= 0), 
 Catches DECIMAL(3,0) NOT NULL CHECK (Catches >= 0), 
 Completions DECIMAL(3,0) NOT NULL CHECK (Completions >= 0),
 Throwaways DECIMAL(2,0) NOT NULL CHECK (Throwaways >= 0),
 Drops DECIMAL(2,0) NOT NULL CHECK (Drops >= 0), 
 Callahans DECIMAL(2,0) NOT NULL CHECK (Callahans >= 0),
 PlayerScore DECIMAL(4,9), NOT NULL CHECK, 
 PRIMARY KEY(Week, Player));

CREATE TABLE Rosters
(UserID DECIMAL(2,0) NOT NULL REFERENCES Users.UserID,  
 Player VARCHAR(256) NOT NULL REFERENCES Players.Player PRIMARY KEY,
 Active CHAR(1) NOT NULL CHECK (Active = 'Y' or Active = 'N'));

CREATE TABLE WeeklyScores
(Week DECIMAL(2,0) NOT NULL CHECK (Week >= 1 and Week <= 17),
 UserID DECIMAL(2,0) NOT NULL REFERENCES Users.UserID,
 TeamScore DECIMAL(4,0) NOT NULL,
 PRIMARY KEY(Week, UserID));

-- Click the About tab 
	-- print a bunch of info

-- Click the Draft tab
SELECT Player, AvgScore, Taken
FROM Players 
ORDER BY Taken, AvgScore DESC, Player

-- Click the Week 'X' tab
	-- print "Team Scores: "
SELECT a.TeamName, a.TeamScore
FROM (WeeklyScores NATURAL JOIN Users) as a
WHERE a.Week = 'X'
ORDER BY a.TeamScore DESC, a.TeamName

	-- print "Player Scores: "
SELECT b.Player, b.PlayerScore, b.TeamName, b.Active
FROM ((PlayerPerformance NATURAL JOIN Roster) as a) NATURAL JOIN Users) as b
WHERE b.Week = 'X'
ORDER BY b.PlayerScore DESC, b.Player

-- Click the User 'X' tab
	-- print "Roster: "
SELECT Player, Active
FROM Rosters
WHERE UserID = 'X'
ORDER BY Player

	-- print "Past results: "
SELECT Week, TeamScore
FROM WeeklyScores 
WHERE UserID = 'X'
ORDER BY Week

-- Click the Leaderboard tab
SELECT a.TeamName, sum(a.TeamScore)
FROM (WeeklyScores NATURAL JOIN Users as a)
GROUP BY a.UserID
ORDER BY sum(a.TeamScore)

-- Click the Final tab
	-- if current_week < 17, print "Season not complete"
SELECT a.TeamName, sum(a.TeamScore)
FROM (WeeklyScores NATURAL JOIN Users as a)
GROUP BY a.UserID
ORDER BY sum(a.TeamScore)

	-- print "Congratulations"
SELECT a.TeamName, max(sum(a.TeamScore))
FROM (WeeklyScores NATURAL JOIN Users as a)
GROUP BY a.UserID



