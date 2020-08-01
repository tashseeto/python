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
    



