import csv

lines = csv.reader('prices.csv')
for line in lines:
  print(line)