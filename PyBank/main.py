import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

month_change = []
timeline = []

net_total = 0
prior_profit_loss = 0
current_profit_loss = 0
change = 0


with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    print('Financial Analysis')
    print('------------------------------------')
    months= len(list(csvreader))
    print('Total Months: '+ str(months))

    for row in csvreader:

      net_total += int(row[1])








    print('Total:{}'.format('$'+ str(net_total)))
    print('------------------------------------')