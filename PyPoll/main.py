import os
import csv

# To get file path
csvpath = os.path.join(".", "Resources","election_data.csv")

# To open file to read
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # To get Header
    csvheader = next(csvreader)
    
    # reset variables to 0
    vote_count = 0
    
    def_candidate_list ={}
    
    candidate_list = []
    candidate_count_list = []

    # To get first row
    first_row = next(csvreader)
    
    # To get count from first row
    vote_count = 1
    
    # To get candidate Name from first row and set its count to 1
    def_candidate_list[first_row[2]] = 1

    # To read a file from next row 
    for row in csvreader:
        
        # To get Total vote count
        vote_count += 1
        
        # To get Candidates and its vote count 
        if(row[2] in def_candidate_list):
            def_candidate_list[row[2]] += 1
        else:
            def_candidate_list[row[2]] = 1

# To print Analysis
print("\nElection Results")
print("----------------------------")
print(f"Total Votes: {vote_count}")
print("----------------------------")

# To print all candidates with total number of votes resp.
for candidate in def_candidate_list:
    print(f"{candidate}: {(def_candidate_list[candidate]/vote_count)*100:.3f}% ({def_candidate_list[candidate]})")

print("----------------------------")

# To print Winner who has max no. of votes
max_key = max(def_candidate_list, key=def_candidate_list.get)
print(f"Winner: {max_key}")
print("----------------------------")