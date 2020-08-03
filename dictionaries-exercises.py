# Question 1

# groceries = {
# "Baby Spinach": 2.78,
# "Hot Chocolate": 3.70,
# "Crackers": 2.10,
# "Facon": 9.00,
# "Carrots": 0.56,
# "Oranges": 3.08
# }

# for item in groceries:
#     print(item, groceries[item])

# def calculate_cost(unit_price, number_purchase):
#     total_unit_cost = unit_price * number_purchase
#     return total_unit_cost

# total = 0

# for item in groceries:
#     item_quantity = input(f"How many units would you like of this item {item}? ")
#     groceries[item] = calculate_cost(groceries[item],int(item_quantity))
#     total += groceries[item]

# total = f"${total:.2f}"

# print("====Izzy's Food Emporium====")
# for item in groceries:
#     print(f"{item:<16} ${groceries[item]:7.2f}")
# print("============================")
# print(f"{total:>25}")

# Question 2

# names = [
# "Maddy", "Bel", "Elnaz", "Gia", "Izzy",
# "Joy", "Katie", "Maddie", "Tash", "Nic",
# "Rachael", "Bec", "Bec", "Tabitha", "Teagen",
# "Viv", "Anna", "Catherine", "Catherine", "Debby",
# "Gab", "Megan", "Michelle", "Nic", "Roxy",
# "Samara", "Sasha", "Sophie", "Teagen", "Viv"
# ]

# 1. Read in the list of names
# 2. For each name
# 3. If I haven't see the name before, add it to a dictionary and set it's value to 0, otherwise increment it's value by 1.
# 4. Output the resulting dictionary.

# names_dict = {}
# for student in names:
#     if student in names_dict:
#         no = int(names_dict[student]) + 1
#         names_dict[student] = no
#     else:
#         names_dict[student] = 1

# for student, no in names_dict.items():
#     print(student, no)
    

# Question 3
# 1. Import csv file
# 2. Create a list
# 3. Each list item is a dictionary with the colour codes
    # - first list is the key & the following lists are the matching values


import csv

def read_csv_file(filepath):
    csv_file = []
    with open(filepath) as file:
        reader = csv.reader(file)
        for line in reader:
            csv_file.append(line)
        return csv_file
   
file = read_csv_file("students/exercise_data/colours_20.csv")
file[0] = [x.strip(' ') for x in file[0]]

# print(file)

# returns as list of lists

#list of keys and values
# keylist = file[0] 
# valuelist = file[1:]

# print(keylist)
# print(valuelist)

# list for holding dictionaries
# create dic for K:V
colour_list = []
for x in file[1:]:
    dic = {}
    # ind is count for the below counter
    # Key & value assignment dic[y] = x[ind]
    ind = 0
    for y in file[0]:
        dic[y] = x[ind] 
        ind += 1
        colour_list.append(dic)

# print(colour_list)

for key, value in colour_list[1].items():
    print(F"{key} : {value}")
# above prints key and value per the formatting

print(colour_list[1])
# above prints dictionary in long row

for x in colour_list[1].items():
    print(x)
# above prints the dictionary on separate row/lines


# ### QUESTION 3 ###
# import csv
# print("***Question 3***")
# def read_csv_file(filepath):
#     """ Take filepath, return content as list """
#     csv_file = []
#     with open(filepath) as file:
#         reader = csv.reader(file)
#         for line in reader:
#             csv_file.append(line)
#     return csv_file
# file = read_csv_file("students/exercise_data/colours_20.csv")
# file[0] = [x.strip(' ') for x in file[0]]


# # colours= []
# # colour_dict = {}
# # for x in file[1:]:
# #     dic = {}
# #     ind = 0
# #     for j in file[0]:
# #         dic[j] = x[ind]
# #         ind += 1
# #     colours.append(dic)


# for x in colours[3].items():
#     print(x)



