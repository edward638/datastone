-- mean goals
SELECT AVG(Goals)
FROM Data
WHERE PlayerName = 'X'

-- mean assists
SELECT AVG(Assists)
FROM Data
WHERE PlayerName = 'X'

-- mean blocks
SELECT AVG(Blocks)
FROM Data
WHERE PlayerName = 'X'

-- mean catches
SELECT AVG(Catches)
FROM Data
WHERE PlayerName = 'X'

-- mean completions
SELECT AVG(Completions)
FROM Data
WHERE PlayerName = 'X'

-- mean throwaways
SELECT AVG(Throwaways)
FROM Data
WHERE PlayerName = 'X'

-- mean drops
SELECT AVG(Drops)
FROM Data
WHERE PlayerName = 'X'

-- standard deviation goals
SELECT STDEVP(Goals)
FROM Data
WHERE PlayerName = 'X'

-- standard deviation assists
SELECT STDEVP(Assists) GROUP BY PlayerName
FROM Data
--WHERE PlayerName = 'X'

-- standard deviation blocks
SELECT STDEVP(Blocks)
FROM Data
WHERE PlayerName = 'X'

-- standard deviation catches
SELECT STDEVP(Catches)
FROM Data
WHERE PlayerName = 'X'

-- standard deviation completions
SELECT STDEVP(Completions)
FROM Data
WHERE PlayerName = 'X'

-- standard deviation throwaways
SELECT STDEVP(Throwaways)
FROM Data
WHERE PlayerName = 'X'

-- standard deviation drops
SELECT STDEVP(Drops)
FROM Data
WHERE PlayerName = 'X'

-- random sample goals
SELECT ROUND(AvgGoals+StdevGoals*(SQRT(-2*LOG(RAND()))*COS(2*PI()*RAND())))
FROM Players
WHERE PlayerName = 'X'

-- random sample assists
SELECT ROUND(AvgAssists+StdevAssists*(SQRT(-2*LOG(RAND()))*COS(2*PI()*RAND())))
FROM Players
WHERE PlayerName = 'X'

-- random sample blocks
SELECT ROUND(AvgBlocks+StdevBlocks*(SQRT(-2*LOG(RAND()))*COS(2*PI()*RAND())))
FROM Players
WHERE PlayerName = 'X'

-- random sample catches
SELECT ROUND(AvgCatches+StdevCatches*(SQRT(-2*LOG(RAND()))*COS(2*PI()*RAND())))
FROM Players
WHERE PlayerName = 'X'

-- random sample completions
SELECT ROUND(AvgCompletions+StdevCompletions*(SQRT(-2*LOG(RAND()))*COS(2*PI()*RAND())))
FROM Players
WHERE PlayerName = 'X'

-- random sample throwaways
SELECT ROUND(AvgThrowaways+StdevThrowaways*(SQRT(-2*LOG(RAND()))*COS(2*PI()*RAND())))
FROM Players
WHERE PlayerName = 'X'

-- random sample drops
SELECT ROUND(AvgDrops+StdevDrops*(SQRT(-2*LOG(RAND()))*COS(2*PI()*RAND())))
FROM Players
WHERE PlayerName = 'X' 

-- score for a player in a given week

SELECT 12*Goals+12*Assists+24*Blocks+0.5*Catches+0.5*Completions-14*Throwaways-14*Drops
FROM PlayerPerformance
WHERE PlayerName = 'X' and Week = 'N'
