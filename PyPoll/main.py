import os
import csv

#join path
election_data = os.path.join("Resources","election_data.csv")

#open and reading the file 
with open(election_data, newline="") as csv_election:
    election_reader = csv.reader(csv_election,delimiter=",")
    election_header = next(csv_election) 


 #???print(f"csv header:(csv_header)")

    #variables

votes =[]
total_votes = 0
candidates_votes =[]
percentage_votes =[]

#create dictionary for candidates
candidates_dictionary = {}

#loopand read throught each row
for candidates in election_reader:

#The total number of votes cast
    #votes.append(candidates[0])
    total_votes = (total_votes+1)
    candidate = (candidates[2])

#A complete list of candidates who received votes
if candidate in candidates_dictionary:candidates_dictionary[candidate]+= 1
else:
     candidates_dictionary[candidate]= 1

    #try #print(candidates_dictionary)




#The percentage of votes each candidate won

##?for key, value in candidates_dictionary.items():
##candidates.append(key)
##candidates_votes.append(value)
##percentage_votes = (round(value/totl_votes*100,3))


#The total number of votes each candidate won


#The winner of the election based on popular vote.

#print analysis election results
##print("Election Results" )
##print("-----------------")
##print('Total Votes')
##print(who got what percentage all 4 candidates)
##print("-----------------")
##print('Winner candidates name')
##print("--------------------")

#create a for loop to iterate through dict and print each key 
for key, value in candidates_dictionary.items():
percentage_votes = (round(candidates_votes/total_votes*100,3))
##print(candidate + ': ' + str(vote_percentage) + '%' + ' (str(candidates_votes)+')')

