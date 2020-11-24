import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    print('Financial Analysis')
    print('---------------------------')
    months= len(list(csvreader))
    print('Total Months: '+ str(months))

with open(csvpath, 'r') as f:
  next(f)
  total = 0
  for row in csv.reader(f):
    total += int(row[1])

  print('Total:{}'.format('$'+ str(total)))