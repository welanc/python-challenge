# Import appropriate modules for this script: 
    # os to navigate to files; 
    # csv to read and write csv files
import os
import csv

# Path to collect data from the Resources folder
election_csv = os.path.join("Resources", "election_data.csv")

# Use with to temporarily open and read election_data.csv
with open(election_csv, "r") as election_file:
    election_csv_reader = csv.reader(election_file, delimiter = ",")

    # Headers: Voter ID,County,Candidate
    # Skip header row
    header = next(election_csv_reader)

    # Variables to calculate total months, net total profit/loss
    votes_total = 0
    khan_votes = 0   
    correy_votes = 0
    li_votes = 0
    otooley_votes = 0
    votes_tally = {}


    # Loop through csv data to calculate total votes,
    for row in election_csv_reader:
        votes_total += 1
        if row[2] == "Khan":
            khan_votes += 1
            votes_tally[row[2]] = khan_votes
        if row[2] == "Correy":
            correy_votes += 1
            votes_tally[row[2]] = correy_votes
        if row[2] == "Li":
            li_votes += 1
            votes_tally[row[2]] = li_votes
        if row[2] == "O'Tooley":
            otooley_votes += 1
            votes_tally[row[2]] = otooley_votes
        
    khan_percent = (khan_votes / votes_total) * 100
    correy_percent = (correy_votes / votes_total) * 100
    li_percent = (li_votes / votes_total) * 100
    otooley_percent = (otooley_votes / votes_total) * 100

    winner = max(votes_tally, key=votes_tally.get)


    print(f"Election Results")
    print(f"-------------------------")
    print(f"Total Votes: {votes_total}")
    print(f"-------------------------")
    print(f"Khan: {round(khan_percent,3)}% ({khan_votes})")
    print(f"Correy: {round(correy_percent,3)}% ({correy_votes})")
    print(f"Li: {round(li_percent,3)}% ({li_votes})")
    print(f"O'Tooley: {round(otooley_percent,3)}% ({otooley_votes})")
    print(f"-------------------------")
    print(f"Winner: {winner}")
    print(f"-------------------------")
    print(votes_tally)

# summate each candidate's dictionary and append that value to a list 
# add each candidate's name to a separate list 
# combine both lists into a dictionary: summated votes as the key, candidate names as the values 
# set a variable equal to the max value of the summated votes
# use dictionary to find the value associated to the max summated votes key 


