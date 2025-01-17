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
    # Read and skip the header row
    csv_header = next(csvfile)
    
    #will store the contents of row 0 into a list named total_vote
    #and contents of row 2 into a list named candidates
    for column in csvreader:
        candidate.append(column[2])
        total_vote.append(column[0])

    vote_count = len(total_vote)
    #counts the number of times the candidate's name appears in the list
    #and stores the value as an integer in individual variables
    khan_votes = int(candidate.count("Khan"))
    correy_votes = int(candidate.count("Correy"))
    li_votes = int(candidate.count("Li"))
    tooley_votes = int(candidate.count("O'Tooley"))

    #calculates the percentage of a candidate's votes against the total vote count
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

     #Compare votes and print winner with the most votes
    if khan_votes>correy_votes>li_votes>tooley_votes:
       Winner = "Khan"
    elif correy_votes >khan_votes>li_votes>tooley_votes:
       Winner = "Correy"
    elif li_votes>khan_votes>correy_votes>tooley_votes:
       Winner = "Li"
    elif tooley_votes>khan_votes>correy_votes>li_votes:
       Winner = "O'Tooley"
    print(f"Winner: {Winner}")
    print('------------------------------')

    #Export results to a text file in the 'Analysis' folder
    poll_results_file = os.path.join("Analysis", "poll_data.txt")
    with open(poll_results_file, "w") as outfile:

      outfile.write("Election Results\n")
      outfile.write("----------------------------\n")
      outfile.write(f"Total Votes: {vote_count}\n")
      outfile.write(f"------------------------------\n")
      outfile.write(f"Khan: {k_percentage}% ({khan_votes})\n")
      outfile.write(f"Correy: {c_percentage}% ({correy_votes})\n")
      outfile.write(f"Li: {l_percentage}% ({li_votes})\n")
      outfile.write(f"O'Tooley: {t_percentage}% ({tooley_votes})\n")
      outfile.write(f"------------------------------\n")
      outfile.write(f"Winner: {Winner}\n")
      outfile.write(f"------------------------------\n")