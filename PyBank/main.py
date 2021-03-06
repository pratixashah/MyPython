import os
import csv

# To get data file
load_file = os.path.join(".", "Resources", "budget_data.csv")

# To set the path for new output file
output_file = os.path.join(".", "Analysis", "PyBank_Analysis.txt")

# reset variables to 0
    
month_count = 0
net_total_amount = 0

greatest__increase_profit_date = ""
greatest__increase_profit = 0

greatest__decrease_profit_date = ""
greatest__decrease_profit = 999999999999999999

first_row_profit = 0
profit_change = 0
total_profit_change = 0
    
# To open file to read
with open(load_file , 'r') as data_file:

    csvreader = csv.reader(data_file, delimiter=',')
    
    # To get Header
    header = next(csvreader)
    
    # To get first row
    first_row = next(csvreader)

    # To get count from first row
    month_count += 1
    net_total_amount += int(first_row[1])
    
    previous_profit = int(first_row[1])  
    
    # To read file from next row
    for row in csvreader:
        
        # To get Month count, Total Amount 
        month_count += 1
        net_total_amount += int(row[1])
        
        # To get Profit Change from currunt and last row
        profit_change = int(row[1]) - previous_profit
        previous_profit = int(row[1])
        
        # To get Total Profit Change
        total_profit_change += profit_change
                    
        # To get Greatest Increase in Profit with its Month resp.
        if(profit_change > greatest__increase_profit):
            greatest__increase_profit_date = row[0]
            greatest__increase_profit = profit_change
        
        # To get Greatest Decrease in Profit with its Month resp.
        if(profit_change < greatest__decrease_profit):
            greatest__decrease_profit_date = row[0]
            greatest__decrease_profit = profit_change

# To print Analysis
output = (
f"\nFinancial Analysis\n"
f"---------------------------------------------"
f"\nTotal Months: {month_count}"
f"\nTotal: ${net_total_amount}"
f"\nAverage Change: ${(total_profit_change/(month_count-1)):.2f} "
f"\nGreatest Increase in Profits: {greatest__increase_profit_date} (${greatest__increase_profit})"
f"\nGreatest Decrease in Profits: {greatest__decrease_profit_date} (${greatest__decrease_profit})"
)

print(output)

# To write result into file

with open(output_file, "w", newline='') as analysis_file:
    analysis_file.write(output)
