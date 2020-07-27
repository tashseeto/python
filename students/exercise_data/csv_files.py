# Question 2

# import csv

# colours_20 = []

# with open("colours_20.csv") as csv_file:
#     reader = csv.reader(csv_file)
#     for line in reader:
#         colours_20.append(line)

# for codes in colours_20:
#     print(f"{codes[1].strip():16} {codes[2].strip():16} {codes[4].strip():16}")


# import csv

# colours_213 = []

# with open("colours_213.csv") as csv_file:
#     reader = csv.reader(csv_file)
#     for line in reader:
#         colours_213.append(line)

# for codes in colours_213:
#     print(f"{codes[1].strip():16} {codes[2].strip():16} {codes[4].strip():16}")


# Question 3a

# import csv

# RGB_data = []

# with open("colours_20.csv") as csv_file:
#     reader = csv.reader(csv_file)
#     for line in reader:
#         RGB_data.append(line)

# red_count = 0
# for colours in RGB_data:
#     count1 = colours[4].count("red")
#     red_count += count1

# green_count = 0
# for colours in RGB_data:
#     count2 = colours[4].count("green")
#     green_count += count2

# blue_count = 0
# for colours in RGB_data:
#     count3 = colours[4].count("blue")
#     blue_count += count3

# print(f"Red: {red_count}")
# print(f"Green: {green_count}")
# print(f"Blue: {blue_count}")


# Question 3b

import csv

RGB_data2 = []

with open("colours_213.csv") as csv_file:
    reader = csv.reader(csv_file)
    for line in reader:
        RGB_data2.append(line)

red_count2 = 0
for colours in RGB_data2:
    count3 = colours[4].count("red")
    red_count2 += count3

green_count2 = 0
for colours in RGB_data2:
    count4 = colours[4].count("green")
    green_count2 += count4

blue_count2 = 0
for colours in RGB_data2:
    count5 = colours[4].count("blue")
    blue_count2 += count5

print(f"Red: {red_count2}")
print(f"Green: {green_count2}")
print(f"Blue: {blue_count2}")