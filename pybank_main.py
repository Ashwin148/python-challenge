import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")
outputfile = os.path.join("budgetoutput.txt")

MonthChangeList =[]
NetChangeList = []
increase = ["",0]
decrease = ["",99999999999]
NetPL = 0


with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    csvheader = next(csvreader)
    firstrow = next(csvreader)

    MonthTotal = 1
    NetPL = NetPL +int(firstrow[1])
    
    prev_net = int(firstrow[1])

    

    for row in csvreader:
        MonthTotal += 1
        NetPL = NetPL +int(row[1])

        netchange = int(row[1]) - prev_net
        prev_net = int(row[1])
        NetChangeList = NetChangeList + [netchange]
        MonthChangeList = MonthChangeList + [row[0]]
        
        if netchange > increase[1]:
            increase[0] = row[0]
            increase[1] = netchange
        if netchange < decrease[1]:
            decrease[0] = row[0]
            decrease[1] = netchange
    
            
MonthAvg = float(sum(NetChangeList)/len(NetChangeList))

f = open("budgetoutput.txt","w")
   
f.write ("Financial Analysis\n")
f.write ("----------------------------\n")
f.write ("Total Months : "+str(MonthTotal)+"\n" ) 
f.write ("Total: "+str(NetPL)+"\n")
f.write ("Average Change: "+str(MonthAvg)+"\n")
f.write ("Greatest Increase in Profits: "+str(increase)+"\n")
f.write ("Greatest Decrease in Profits: "+str(decrease)+"\n")                   


       
         

 