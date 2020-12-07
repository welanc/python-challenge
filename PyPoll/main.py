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

    # Variables to calculate: total votes, votes per candidate, 
        # Dictionary with candidate names as keys and their total vote as values
    votes_total = 0
    khan_votes = 0   
    correy_votes = 0
    li_votes = 0
    otooley_votes = 0
    votes_tally = {}


    # Loop through csv data to calculate total votes, votes per candidate
        # and incrementally updating the votes tally dictionary with each candidate's votes 
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


    # Calculate vote percentage for each candidate     
    khan_percent = (khan_votes / votes_total) * 100
    correy_percent = (correy_votes / votes_total) * 100
    li_percent = (li_votes / votes_total) * 100
    otooley_percent = (otooley_votes / votes_total) * 100

    # Searching for the max value in the votes tally dictionary 
        # to get the key (winning candidate)
    winner = max(votes_tally, key=votes_tally.get)

    # Output election results to Terminal
    print(f"Election Results")
    print(f"-------------------------")
    print(f"Total Votes: {votes_total}")
    print(f"-------------------------")
    print(f"Khan: {khan_percent:.3f}% ({khan_votes})")
    print(f"Correy: {correy_percent:.3f}% ({correy_votes})")
    print(f"Li: {li_percent:.3f}% ({li_votes})")
    print(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
    print(f"-------------------------")
    print(f"Winner: {winner}")
    print(f"-------------------------")

# Write to a .txt file
    output_txt = os.path.join("Analysis", "pypoll_output.txt")

# Edit the .txt file with the election results
with open(output_txt, "w", newline ="") as out_file:
    output_txt_writer = csv.writer(out_file)

    output_txt_writer.writerow([f"Election Results"])
    output_txt_writer.writerow([f"-------------------------"])
    output_txt_writer.writerow([f"Total Votes: {votes_total}"])
    output_txt_writer.writerow([f"-------------------------"])
    output_txt_writer.writerow([f"Khan: {khan_percent:.3f}% ({khan_votes})"])
    output_txt_writer.writerow([f"Correy: {correy_percent:.3f}% ({correy_votes})"])
    output_txt_writer.writerow([f"Li: {li_percent:.3f}% ({li_votes})"])
    output_txt_writer.writerow([f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})"])
    output_txt_writer.writerow([f"-------------------------"])
    output_txt_writer.writerow([f"Winner: {winner}"])
    output_txt_writer.writerow([f"-------------------------"])