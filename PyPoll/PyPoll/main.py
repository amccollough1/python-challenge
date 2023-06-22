import os
import csv
#print formatted data 
print ("" " ")
print("Election Results \n")
print("------------------------- \n")
#set path for file
electioncsv = os.path.join('Resources', 'election_data.csv')
#open csv
with open (electioncsv) as csvfile:
    csvreader= csv.reader(csvfile, delimiter=',')
    csv_header=next(csvreader)
    #list to store data 
    votes=[]
    candi1=[]
    candi2=[]
    candi3=[]
    #initialize counter for each candidate 
    candidate1=0
    candidate2=0
    candidate3=0

    #read through each row after header
    for row in csvreader:
        #Add votes of column A from data set 
        votes.append(row[0])
        
        #Find candidate name (as value) and add counter for how many times the value appears and append the value to an empty list 
        if row[2] == "Charles Casper Stockham":
            candidate1 +=1
            candi1.append(row[2])
        elif row[2] == "Diana DeGette":
            candidate2 +=1 
            candi2.append(row[2])
        elif row [2] == "Raymon Anthony Doane":
            candidate3 +=1   
            candi3.append(row[2])       


        
        

     #Assign variables total_votes to len    
    total_votes=len(votes) 
    perc1=len(candi1)
    perc2=len(candi2)
    perc3=len(candi3)
    #calculate percentages
    newval=(perc1/total_votes)*100
    newval2=(perc2/total_votes)*100
    newval3=(perc3/total_votes)*100
    #Find the winner fo the election 
    if perc1> perc2 and perc3:
        winner="Charles Casper Stockham"
    elif perc2> perc1 and perc3:
        winner= "Diana DeGette"
    else :
        winner="Raymon Anthony Doane"
    
    #print results
    print("Total Votes: " + str(total_votes))
    print("-------------------------\n")
    print("Charles Casper Stockham: "  + str(round(newval,3)) + "%" + " (" + str(candidate1)+ ")" )
    print("Diana DeGette: "+ str(round(newval2,3)) + "%" + " (" + str(candidate2)+ ")" )
    print("Raymon Anthony Doane: "+ str(round(newval3,3)) + "%" + " (" + str(candidate3)+ ")" )
    print("-------------------------\n")

    #Print the winner of the election based on popular vote
    print("Winner: " + str(winner))

    print("-------------------------\n")

#write to txt file
output= open('output.txt',  "w")
output.write("Election Results \n")
output.write("------------------------- \n")
output.write("Total Votes: " + str(total_votes) + "\n")
output.write("------------------------- \n")
output.write("Charles Casper Stockham: "  + str(round(newval,3)) + "%" + " (" + str(candidate1)+ ")\n" )
output.write("Diana DeGette: "+ str(round(newval2,3)) + "%" + " (" + str(candidate2)+ ")\n" )
output.write("Raymon Anthony Doane: "+ str(round(newval3,3)) + "%" + " (" + str(candidate3)+ ")\n" )
output.write("-------------------------\n")
output.write("Winner: " + str(winner) + "\n")
output.write("-------------------------")
output.close()