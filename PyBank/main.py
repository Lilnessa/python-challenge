# PyBank 
# Create a Python script to analyze the financial records of your company. 
# You will be given a financial dataset called budget_data.csv. 
# The dataset is composed of two columns: "Date" and "Profit/Losses".

import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join("PyBank", "Resources","budget_data.csv")

# Variables
value = 0
change = 0
TotalMon = 0
TotalValue = 0
avgchange = 0
pnl_change = 0
prior_pnl = 0
pnl_list = []

# Open and read the CSV file then delimiter split and identify header
with open(budget_csv) as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csv_file)

#loop and store data in dictionary
    for row in csv_reader:
        pnl_list.append({"date": row[0],"value": row[1],"change": 0})

# Part1----------------------------------------------------
# The total number of months included in the dataset (Total Months: 86)

    TotalMon = len(pnl_list)

# Part2----------------------------------------------------
# The net total amount of "Profit/Losses" over the entire period (Total: $22564198)
with open(budget_csv) as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter=',')

    for row in csv_reader:
        
        # TotalValue = sum(int(row[1]) for row in csv_reader)
        TotalValue = sum(int(row["value"]) for row in pnl_list)

# Part3----------------------------------------------------
# The changes in "Profit/Losses" over the entire period, and then the 
# average of those changes avgchange (Average Change: $-8311.11)

with open(budget_csv) as csv_file: 
    csv_reader = csv.reader(csv_file, delimiter=',')
        
    prior_pnl = pnl_list[0]["value"]
    offset = 1
    for i in range(offset,TotalMon):
        # print(i)
        pnl_list[i]["change"] = int(pnl_list[i]["value"]) - int(prior_pnl)
        prior_pnl = pnl_list[i]["value"]
        pnl_change = pnl_list[i]["change"]
        # print(pnl_list)
        # print(prior_pnl)
        # print(pnl_change)
      
    total_pnl_change = sum(int(row['change']) for row in pnl_list)
    avgchange = total_pnl_change / (TotalMon - 1)
    # print(f"Total PNL change: {total_pnl_change}")

# Part4----------------------------------------------------
# The greatest increase in profits (date and amount) over the entire period
# gincrease_date (Greatest Increase in Profits: Aug-16 ($1862002))

gincrease = max(pnl_list,key=lambda x:x['change'])
# print(gincrease_value)

# The greatest decrease in profits (date and amount) over the entire period
# gdecrease_date (Greatest Decrease in Profits: Feb-14 ($-1825558))

gdecrease = min(pnl_list,key=lambda x:x['change'])
# print(gdecrease_value)

# Print to ternminal and export Text to file -----------------
print("\nFinancial Analysis\n")
print("----------------------------\n")
print(f"Total Months: {TotalMon}\n")
print(f"Total: ${TotalValue:,}\n")
print(f"Average: ${avgchange:,.2f}\n")
print(f"Greatest Increase in Profits: {gincrease['date']} (${gincrease['change']:,})\n")
print(f"Greatest Increase in Profits: {gdecrease['date']} (${gdecrease['change']:,})\n")

result_txt = os.path.join("PyBank", "analysis","PyBank_result.txt")
with open(result_txt,"w") as text_file:
    text_file.write(os.linesep +"Financial Analysis"+ os.linesep)
    text_file.write("----------------------------"+ os.linesep)
    text_file.write(f"Total Months: {TotalMon}"+ os.linesep)
    text_file.write(f"Total: ${TotalValue:,}"+ os.linesep)
    text_file.write(f"Average: ${avgchange:,.2f}"+ os.linesep)
    text_file.write(f"Greatest Increase in Profits: {gincrease['date']} (${gincrease['change']:,})"+ os.linesep)
    text_file.write(f"Greatest Increase in Profits: {gdecrease['date']} (${gdecrease['change']:,})"+ os.linesep)
