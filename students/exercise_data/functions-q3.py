# Question 3

import csv

def read_csv_file(filepath):
    colours = []
    with open(filepath) as csv_file:
        reader = csv.reader(csv_file)
        for line in reader:
            colours.append(line)
        return colours
   

colours = read_csv_file("colours_20.csv")
colours = read_csv_file("colours_213.csv")
print(colours)


def format_colour_line(colour_data):
    for codes in colour_data:
        print(f"{codes[1].strip():18} {codes[2].strip():18} {codes[4].strip():18}")


format_colour_line(colours)
