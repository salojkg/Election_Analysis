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

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Print each row in the CSV file.
    for row in file_reader:
        print(row)
     

