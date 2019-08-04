import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")
outputfile = os.path.join("polloutput.txt")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    Vote_Total = 0
    CandidateList = []
    CandidateVotes = []
    CPercent = []
    #Winner = 0
    MaxVotes = 0
    finallist = ""

    for row in csvreader:

        Vote_Total += 1

        if row[2] in CandidateList:
            name = row[2]
            indexAmt = CandidateList.index(name)
            CandidateVotes[indexAmt] += 1
        else:
            CandidateList.append(row[2])
            CandidateVotes.append(1)
    
    for row in range(len(CandidateVotes)):

        CandidateVotes[row]/Vote_Total
        CPercent = CandidateVotes[row]/Vote_Total
        
        print (CandidateList[row] + ": " + str(round(CPercent,2)) + " " + str(CandidateVotes[row]))
        finallist += CandidateList[row] + ": " + str(round(CPercent,2)) + " " + str(CandidateVotes[row]) + "\n"
        #print (finallist)
    
    MaxVotes = max(CandidateVotes)

    indexWinner = (CandidateVotes.index(MaxVotes))

    Winner = (CandidateList[indexWinner])

f = open("polloutput.txt","w")

f.write ("Election Results\n")
f.write ("----------------------------\n")
f.write ("Total Votes: "+ str(Vote_Total) +"\n" ) 
f.write ("----------------------------\n")
f.write (" "+str(finallist)+"\n")
f.write ("----------------------------\n")
f.write ("Winner: "+str(Winner)+"\n")
f.write ("----------------------------\n")

        


    






#print (CandidateList)
#print (CPercent)
#print (CandidateVotes)