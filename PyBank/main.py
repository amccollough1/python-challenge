import os
import csv
#print formatted data 
print ("" " ")
print("Financial Analysis")
print("------------------------------")
#set path for file
budgetcsv = os.path.join('Resources', 'budget_data.csv')
#open csv
with open (budgetcsv) as csvfile:
    csvreader= csv.reader(csvfile, delimiter=',')
    csv_header=next(csvreader)
    #list to store data
    months=[]
    net_total=[]

    #read through each row after header
    for row in csvreader:
        #Add months of column A from data set 
        months.append(row[0])
        #Add net total amount of column B from data set 
        net_total.append(int(row[1]))
     #Assign variable total_months to the length of months add to the open list.    
    total_months=len(months) 
    #print format 
    print("Total Months: " + str(total_months))
    #sum the net total of profit/losses
    print("Total: $" + str(sum(net_total)))
    #Add average change
    avg_change= []
    #calculate changes in average 
    for avg in range(1, len(net_total)):
        avg_change.append((int(net_total[avg])- int(net_total[avg-1])))
    rev_avg=round(sum(avg_change)/ len(avg_change),2)

    print("Average change: $ " + str(rev_avg))  
    #calculate greatest increase/decrease 
    greatest_inc = max(avg_change)
    greatest_dec = min(avg_change)
    print ("Greatest Increase in Profits: " + str(months[avg_change.index(max(avg_change))+1]) + " ($ " + str(greatest_inc)+ ")")
    print ("Greatest Decrease in Profits: " + str(months[avg_change.index(min(avg_change))+1]) + " ($ " + str(greatest_dec)+ ")")


#write to txt file
output= open('output.txt',  "w")
output.write("Financial Analysis \n")
output.write("--------------------\n")
output.write("Total Months: " + str(total_months) + "\n")
output.write("Total: $" + str(sum(net_total))+ "\n")
output.write("Average change: $ " + str(rev_avg) +"\n")
output.write("Greatest Increase in Profits: " + str(months[avg_change.index(max(avg_change))+1]) + " ($ " + str(greatest_inc)+ ") \n")
output.write("Greatest Decrease in Profits: " + str(months[avg_change.index(min(avg_change))+1]) + " ($ " + str(greatest_dec)+ ") \n")
output.close()
