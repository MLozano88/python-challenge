import os
import csv

candidate = []
total_vote = []


#Path used to collect data from resources
csvpath = os.path.join('Resources', 'election_data.csv')

#Read module
with open(csvpath, newline="") as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvfile)
    
    #will store the contents of row 2 into a list named candidates
    for column in csvreader:
        candidate.append(column[2])
        total_vote.append(column[0])

    vote_count = len(total_vote)
    #counts the number of times the candidate's name appears in column 2
    khan_votes = int(candidate.count("Khan"))
    correy_votes = int(candidate.count("Correy"))
    li_votes = int(candidate.count("Li"))
    tooley_votes = int(candidate.count("O'Tooley"))

    #calculate the percentage of a candidate's vote total
    k_percentage = round((khan_votes/vote_count) * 100)
    c_percentage = round((correy_votes/vote_count) * 100)
    l_percentage = round((li_votes/vote_count) * 100)
    t_percentage = round((tooley_votes/vote_count) * 100)

    print('Election Results')
    print('------------------------------')
    print(f'Total Votes: {vote_count}')
    print('------------------------------')
    print(f"Khan: {k_percentage}% ({khan_votes})")
    print(f"Correy: {c_percentage}% ({correy_votes})")
    print(f"Li: {l_percentage}% ({li_votes})")
    print(f"O'Tooley: {t_percentage}% ({tooley_votes})")
    print('------------------------------')