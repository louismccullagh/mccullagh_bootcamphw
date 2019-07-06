import os
import csv

data = os.path.join("Resources", "budget_data.csv")


with open(data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvfile)
    print(f"Header: {header}")


    Profit = []
    Months = []
    for rows in csvreader:
        Profit.append(int(rows[1]))
        Months.append(rows[0])


    Delta_Revenue = []
    for x in range(1, len(Profit)):
        Delta_Revenue.append((int(Profit[x]) - int(Profit[x-1])))
    
    
    Revenue_Avg = ((sum(Delta_Revenue)) / (len(Delta_Revenue)))
    Total_Months = len(Months)
    Increase = max(Delta_Revenue)
    Decrease = min(Delta_Revenue)


    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(Total_Months))
    print("Total: $" + str(sum(Profit)))
    print("Average Change: $" + str(Revenue_Avg))
    print("Greatest Increase in Profits: " + str(Months[Delta_Revenue.index(max(Delta_Revenue))+1]) + " $" + str(Increase))
    print("Greatest Decrease in Profits: " + str(Months[Delta_Revenue.index(min(Delta_Revenue))+1]) + " $" + str(Decrease))



    file = open("pybank.txt","w")
    file.write("Financial Analysis" + "\n")
    file.write("----------------------------" + "\n")
    file.write("Total Months: " + str(Total_Months) + "\n")
    file.write("Total: $" + str(sum(Profit)) + "\n")
    file.write("Average Change: $" + str(Revenue_Avg) + "\n")
    file.write("Greatest Increase in Profits: " + str(Months[Delta_Revenue.index(max(Delta_Revenue))+1]) + " $" + str(Increase) + "\n")
    file.write("Greatest Decrease in Profits: " + str(Months[Delta_Revenue.index(min(Delta_Revenue))+1]) + " $" + str(Decrease))
    file.close()

