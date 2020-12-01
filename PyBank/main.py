import os
import csv

#Defined variables
profit_loss = []
timeline = []


net_total = 0
prior_profit_loss = 0
current_profit_loss = 0
change = 0
row_count = 0

#Path used to collect data from resources
csvpath = os.path.join('Resources', 'budget_data.csv')

#Read module
with open(csvpath, newline="") as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvfile)

    for row in csvreader:

      #Count through the number of rows
      row_count += 1

      current_profit_loss = int(row[1])
      net_total += current_profit_loss

      if (row_count == 1):
        prior_profit_loss = current_profit_loss
        continue

      else:
        change = current_profit_loss - prior_profit_loss

        timeline.append(row[0])

        profit_loss.append(change)

        prior_profit_loss = current_profit_loss
    
      total_profit_loss = sum(profit_loss)
      total_average = round(total_profit_loss/(row_count - 1), 2)

      greatest_increase = max(profit_loss)
      greatest_decrease = min(profit_loss)

      greatest_month_index = profit_loss.index(greatest_increase)
      lowest_month_index = profit_loss.index(greatest_decrease)

      most_profit = timeline[greatest_month_index]
      most_loss = timeline[lowest_month_index]

    print('Financial Analysis')
    print('------------------------------------')
    print(f'Total Months: {row_count}')
    print(f'Total: ${net_total}')
    print(f"Average Change:  ${total_average}")
    print(f"Greatest Increase in Profits:  {most_profit} (${greatest_increase})")
    print(f"Greatest Decrease in Profits:  {most_loss} (${greatest_decrease})")
    print('------------------------------------')

    budget_write_file = os.path.join("Analysis", "budget_data.txt")
    with open(budget_write_file, "w") as outfile:

      outfile.write("Financial Analysis\n")
      outfile.write("----------------------------\n")
      outfile.write(f"Total Months:  {row_count}\n")
      outfile.write(f"Total:  ${net_total}\n")
      outfile.write(f"Average Change:  ${total_average}\n")
      outfile.write(f"Greatest Increase in Profits:  {most_profit} (${greatest_increase})\n")
      outfile.write(f"Greatest Decrease in Losses:  {most_loss} (${greatest_decrease})\n")