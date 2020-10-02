import os
import csv

budget_data = os.path.join("Resources", "budget_data.csv")

with open(budget_data, newline="") as csv_budget:
    budget_reader = csv.reader(csv_budget,delimeter=',')

   ## print(csvreader)
    budget_header = next(csv_budget)##or budget_reader)

##with open(csvpath, newline='') as csvfile:
    ##csvreader = csv.reader(csvfile,delimeter=",")
    ##print(cvsreader)
    
    ##csv_header = next(csvreader)
    ##print(f"CSV Header: {csv_header}")

#variables
total_months = 0
rev = []
date = []
totalrev = 0 
averagechange = 0
totalrevchange = 0
#total_profit = 0
#total_loss = 0
greatestincrease_amt = 0
greatestdecrease_amt = 0
previousamount =  0
difference = 0
diflist = []

#The total number of months included in the dataset

for row in csv_budget:## csvreader or csv_budget?

    date.append(row[0])
    totalrev.append(row[1])
    total_months = total_months + 1


#The net total amount of "Profit/Losses" over the entire period
totalrev = totalrev + int(row[1])


#The average of the changes in "Profit/Losses" over the entire period
#average change = row B4-B3 in excel
##averagechange = int(row[1)]) ##??
difference = averagerevchange - previousamount
differencelist.append(difference)
previousamount = averagerevenuechange

#The greatest increase in profits (date and amount) over the entire period
#sum of all the differnces and the highest amount one 
if averagerevechange > greatestincrease_amt:
     greatestincrease_amt = averagerevchange
     max_months = row[0]

if averagerevchange < greatestdecrease_amt:
    greatestdecrease_amt = averagerevchange
    min_months = row[0]

#The greatest decrease in losses (date and amount) over the entire period
#sum of all differences and the least amount 

#print on screen summary
##print("Financial Analysis")
##print("--------------------")
##print("Total Months:" + str(row_month)
##print("Total: $" + str(total_budg))
##print("Average Change: $" + str(round(avg_")
##print("Greatest Increase in profits:" + max_increase_month) + " (" + str(max_increase) + ")").....???
##print("Greatest Decrease in profit:" + )
