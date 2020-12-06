import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join("Resources", "budget_data.csv")

# Use with to temporarily open and read budget_data.csv
with open(budget_csv, "r") as budget_file:
    budget_csv_reader = csv.reader(budget_file, delimiter = ",")
    
    # Skip header row
    header = next(budget_csv_reader)
    
    # Variables to calculate total months, net total profit/loss
    months_total = 0
    profit_loss_total = 0
    profit_loss_monthly = []
    p_l_month = []
    difference = []


    for row in budget_csv_reader:
        months_total += 1
        profit_loss_total += int(row[1])
        p_l_month.append(row[0])
        profit_loss_monthly.append(int(row[1]))


    for x in range(1,len(profit_loss_monthly)):
        diff = profit_loss_monthly[x]-profit_loss_monthly[x-1]
        difference.append(int(diff))
        max_diff = max(difference)
        min_diff = min(difference)
        

     
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {months_total}")
    print(f"Total: ${profit_loss_total}")
    print(f"Average Change: ${round(sum(difference)/len(difference),2)}")
    print(f"Greatest Increase in Profits: {p_l_month[difference.index(max_diff) + 1]} (${max_diff})")
    print(f"Greatest Decrease in Profits: {p_l_month[difference.index(min_diff) + 1]} (${min_diff})")   


# write to a .txt file