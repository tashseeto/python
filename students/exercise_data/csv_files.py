# import csv

# colours_20 = []

# with open("colours_20.csv") as csv_file:
#     reader = csv.reader(csv_file)
#     for line in reader:
#         colours_20.append(line)

# for codes in colours_20:
#     print(f"{codes[1].strip():16} {codes[2].strip():16} {codes[4].strip():16}")


import csv

colours_213 = []

with open("colours_213.csv") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        colours_213.append(line)

for codes in colours_213:
    print(f"{codes[1].strip():16} {codes[2].strip():16} {codes[4].strip():16}")