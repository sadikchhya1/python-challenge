import os
import csv


#define
#votes = []
#name = []
total_votes = 0
votecount = []
candidates = []
percentage = {}
winnercount = 0
#candidates_dictionary = {}

#join path
csvpath = os.path.join("Resources","election_data.csv")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    next(csvreader) 
    #open and reading the file 
     #loopand read throught each row
    for row in csvreader:
      #votes.append(candidates[0])
         total_votes += 1
         if (row[2]) not in candidates:
            candidates.append(row[2])
            votecount.append(0)


         candidateIndex = candidates.index(row[2])
         votecount[candidateIndex] += 1

            #calculating percentage

    #for key, value in votecount.items():
        #percentage[key] = str(round((value/total_votes)*100),3) + "% ("+str(value)+ ")"


        #The total number of votes each candidate won


    #The winner of the election based on popular vote.

#print analysis election results
print("\nElection Results")    
print("-----------------")
print("Total Votes:{total_votes}")
##print("-----------------")
##print(who got what percentage all 4 candidates)
##print('Winner candidates name')
##print("--------------------")

#create a for loop to iterate through dict and print each key 
#for key, value in candidates_dictionary.items():
#percentage_votes = (round(candidates_votes/total_votes*100,3))
##print(candidate + ': ' + str(vote_percentage) + '%' + ' (str(candidates_votes)+')')

#output to text file 
#save_file =  "ElectionData.txt"
#svpath = os.path.join("analysis", save_file)
#with open(csvpath,'w') as text:
    #text.write("\nElection Results")
    #text.write("\n-----------------")
    #text.write("\nTotal Votes:" + str(total_votes)