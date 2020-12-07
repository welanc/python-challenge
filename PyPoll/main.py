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
    votes_total = int()
    khan_votes = {}   
    correy_votes = {}
    li_votes = {}
    otooley_votes = {}


    # Loop through csv data to calculate total votes,
    for row in election_csv_reader:
        votes_total += 1
        if row[2] == "Khan":
            khan_votes[str(row[0])] = int(1)
        if row[2] == "Correy":
            correy_votes[str(row[0])] = int(1)
        if row[2] == "Li":
            li_votes[str(row[0])] = int(1)
        if row[2] == "O'Tooley":
            otooley_votes[str(row[0])] = int(1)
    
    khan_percent = (sum(khan_votes.values()) / votes_total) * 100
    correy_percent = (sum(correy_votes.values()) / votes_total) * 100
    li_percent = (sum(li_votes.values()) / votes_total) * 100
    otooley_percent = (sum(otooley_votes.values()) / votes_total) * 100

    print(f"Election Results")
    print(f"-------------------------")
    print(f"Total Votes: {votes_total}")
    print(f"-------------------------")
    print(f"Khan: {round(khan_percent,3)}% ({sum(khan_votes.values())})")
    print(f"Correy: {round(correy_percent,3)}% ({sum(correy_votes.values())})")
    print(f"Li: {round(li_percent,3)}% ({sum(li_votes.values())})")
    print(f"O'Tooley: {round(otooley_percent,3)}% ({sum(otooley_votes.values())})")
    print(f"-------------------------")
    print(f"Winner: ")
    print(f"-------------------------")
    

# summate each candidate's dictionary and append that value to a list 
# add each candidate's name to a separate list 
# combine both lists into a dictionary: summated votes as the key, candidate names as the values 
# set a variable equal to the max value of the summated votes
# use dictionary to find the value associated to the max summated votes key 


