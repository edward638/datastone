/data/ : This directory contains all of the data necessary for our project.

/rawdata/ : This directory contains all of the csv files downloaded from the ultianaltyics website.

/datafix.py : This python script generates the relevant statistics for each player in the raw data. The results are stored under the fixed data directory. It only has to be run ONCE after the raw data directory is complete. Run using "py datafix.py" in the command line.

/fixeddata/ : This directory contains the fixed or conveniently reorganized version of the data.

/datapoll.py : This python script simulates a week of new statistics by first generating a poisson distribution based on the data found in the fixed data directory then polling from that distribution. The results are stored under the polled data directory. It should be run once for each week to be simulated. Run using "py datapoll.py wk_no" in the command line. 'wk_no' must be a positive integer.

/polleddata/ : This directory contains the polled or simulated data to be used for the weekly scores.