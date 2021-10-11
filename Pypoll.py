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

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

      # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
     # 2. Add to toal vote count
        total_votes += 1

        print(total_votes)
     

