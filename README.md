# Overview of Election Audit
The Overview of this Election Audit project is to provide the Election commission with some additional inputs which is detailed below.:

- The voter turnout for each county
- The percentage of votes from each county out of the total count
- The county with the highest turnout

We have already analyszed the data for the below
- Total number of Votes
- County wise Votes for each candidate and their vote percentage
-  Winner Vote count and winning percentage
# Election Audit Results 

- Total Votes: 369,711

- County Votes Perecntage & Votes:
   - Jefferson: 10.5% (38,855)
   - **Denver: 82.8% (306,055)**
   - Arapahoe: 6.7% (24,801)

- Largest County Turnout: **Denver**

- Candidates Votes percentage & number of Votes
  - Charles Casper Stockham: 23.0% (85,213)
  - **Diana DeGette: 73.8% (272,892)**
  - Raymon Anthony Doane: 3.1% (11,606)

- Election Winner and Winning Statistics
  - Winner: **Diana DeGette**
  - Winning Vote Count: **272,892**
  - Winning Percentage: **73.8%**

# Election Audit Summary

This code can be reused for analyzing the result of any elctions with the same csv file format. Here are my two ways which we can accomplish

Static Code Change:

- Copy new details file to Reseources folder. Eg: election_results_new.csv. Edit line 10 in PyPoll_Challenge.py to update the new file name.

      #file_to_load = os.path.join("Resources", "election_results.csv")
      
      file_to_load = os.path.join("Resources", "election_results_new.csv")

Dynamic Code Change

- Use input function to get the file path for the new election results file and read the file. 

      #file_to_load = os.path.join("Resources", "election_results.csv")
      
      file_to_load = input("Enter file path")
      
      Output:
      Enter file path C:/Users/Saloj/Desktop/election_results_new.csv (Demonstartion purpose only, sample path)


 
