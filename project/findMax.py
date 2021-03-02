import csv
with open('data\co2_emission.csv', 'r') as f:
    next(f)
    reader = csv.reader(f)
    maxnum = max(reader, key=lambda row: float(row[3]))
print(maxnum)