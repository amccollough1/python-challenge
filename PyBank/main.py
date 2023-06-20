import os
import csv

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
        months.append(row[0])
        net_total.append(int(row[1]))
    total_months=len(months) 
    
    print("Total Months: " + str(total_months))
    print("Total: $" + str(sum(net_total)))

    avg_change= []
    for avg in range(1, len(net_total)):
        avg_change.append((int(net_total[avg])- int(net_total[avg-1])))
    rev_avg=round(sum(avg_change)/ len(avg_change),2)

    print("Average change: $ " + str(rev_avg))  

    greatest_increase = max(avg_change)
    greatest_decrease = min(avg_change)
    print ("Greatest Increase in Profits: " + str(months[avg_change.index(max(avg_change))+1]) + " ($ " + str(greatest_increase)+ ")")
    print ("Greatest Decrease in Profits: " + str(months[avg_change.index(min(avg_change))+1]) + " ($ " + str(greatest_decrease)+ ")")
