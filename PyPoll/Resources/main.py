import os
import csv

#reading our csv file
path_way = os.path.join('../Resources/election_data.csv')
#print(path_way)

#variables utilized
ballot_list= []
candidate_list = []
total_votes = 0
voter_percent = 0
candidate_votes = {}
voter_count = []
nominee = 0
poll_count = 0
voting_results = 0
win_amount = 0
winner = 0

#open file
with open(path_way) as csvfile:
    csv_header = next(csvfile)
    #use csv.reader function to read in csvfile
    csv_reader = csv.reader(csvfile, delimiter=",")
    for row in csv_reader:
        #cycled through row to get the total number of votes
        total_votes +=1
        #candidates names
        candidate_name = row[2]
        #if the candidate name doesn't match, then add to a list named candidate list
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            #count the amount of votes each candidate received
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name]+= 1 
    #print total amount of votes received
    print(total_votes)
    # election = (
    #     f"Election Results\n"
    #     f"-------------------------------\n"
    #     f"Total Votes: {total_votes}\n"
    #     f"-------------------------------\n"
    #     )
    # print(election)
    #loop throgh the names of the list
    for nominee in candidate_votes:
        poll_count = candidate_votes.get(nominee)
        #find the percent of votes each candidate received
        voter_percent = float(poll_count) / float(total_votes)*100
        #find the winner
        if (poll_count > win_amount):
            win_amount = poll_count
            winner = nominee
        #create a table for the poll results that include the nominees, the percentage won by (out by 3 decimal places), and the number of votes
        voting_results = f"{nominee}: {voter_percent:.3f}% ({poll_count})\n"
        print(voting_results)
    print(f"Winner: {winner}\n")

    




       
    

    




