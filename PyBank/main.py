import os
import csv

budget_data = os.path.join("Resources", "budget_data.csv")

with open(budget_data) as csv_budget:
    budget_reader = csv.reader(csv_budget)
    next(budget_reader)
   
    #print(cvsreader)
    
     #variables/define
    total_months = 0
    rev = []
    date = []
    totalrev = 0 
    averagechange = 0
    totalrevchange = 0
    #total_profit = 0
    #total_loss = 0
    greatestincrease_amt = 0
    greatestinc_month = 0
    greatestdecrease_amt = 0
    greatesedec_month = 0
    previousrev =  0
    currentrev = 0
    difference = 0
    difflist = []
    

    #The total number of months included in the dataset
    #Loop

    for row in budget_reader:
        total_months += 1
        totalrev += int(row[1])
       
    #date.append(row[0])
        # totalrev.append(row[1])
       
        #The average of the changes in "Profit/Losses" over the entire period
    
        if total_months == 1:
            difference = 0
        else:
            difference = int(row[1]) - previousrev
        
        previousrev = int(row[1]) 
        difflist.append(difference)
    averagechange = (sum(difflist)/(total_months-1))
       
    #The greatest increase in profits (date and amount) over the entire period
        
        #greatestincrease_amt = max(difference)
        #greatestinc_month = str(date[difference.index(max(difference))])
      
    #The greatest decrease in losses (date and amount) over the entire period
    #sum of all differences and the least amount 

        # greatestdecrease_amt = min(difference)
         #greatestdec_month = str(date[difference.index9min9difference))])

    #print on screen summary
    print("\nFinancial Analysis")
    print("--------------------")
    print("Total Months:" + str(total_months))
    print("Total: $" + str(totalrev))
    print("Average Change: $" + str(round(averagechange ,2)))
    print("Greatest Increase in profits")
    print("Greatest Decrease in profits")

#output to a text file
save_file = "Bankfile.txt"
csvpath = os.path.join("Analysis", save_file)
with open(csvpath,'w') as text:
    text.write("\nFinancial Analysis")
    text.write("\n--------------------")
    text.write("\nTotal Months:" + str(total_months))
    text.write("\nTotal: $" + str(totalrev))
    text.write("\nAverage Change: $" + str(round(averagechange ,2)))
    text.write("\nGreatest Increase in profits")
    text.write("\nGreatest Decrease in profits")