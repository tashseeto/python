# Question 3

import csv

colours_20 = []

with open("colours_20.csv") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        colours_20.append(line)

print(colours_20)