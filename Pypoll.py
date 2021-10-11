# The total number of votes cast
# A Complete list of candidates who received votes
# The precentage of votes each candidates won
# The total number of votes each candidates won
# The winner of the election based on popular votes
# Open the election results and read the file
import os
import csv
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# 1. Initialize a total vote counter
total_votes=0
# Candidate Options
candidate_options = []

# 1. Declare the empty dictionary.
candidate_votes = {}

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

      # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
     # 2. Add to toal vote count
        total_votes += 1
# Print the candidate name from each row.
        candidate_name = row[2]

         # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
    # 2. Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
# Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

# Print the candidate vote dictionary.
print(candidate_votes)
     

