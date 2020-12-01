import os
import csv

khan = []
correy = []
li = []
tooley = []

total_vote = 0


#Path used to collect data from resources
csvpath = os.path.join('Resources', 'election_data.csv')

#Read module
with open(csvpath, newline="") as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvfile)

    for row in csvreader:
        
        total_vote += 1

    
    print('Election Results')
    print('------------------------------')
    print(f'Total Votes: {total_vote}')
    print('------------------------------')