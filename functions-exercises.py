# Question 1

# def temperature(celsius):
#     celsius = (celsius - 32) / 1.8
#     celsius = round(celsius)
#     print(celsius)

# # temperature(32)
# # temperature(113)
# # temperature(26.6)

# # # Question 2


# # list for user input


# num_list = []

# number = input("Please enter a number: ")

# total_sum = 0
# count = 0
# while len(number) > 0:
#     count += 1
#     total_sum += int(number)
#     num_list.append(number)
#     number = input("Please enter another number: ")
    
# num_items = len(num_list)
# num_list2 = int(num_items)

# # print(num_list2)
# # print(num_items)
# # print(total_sum)

# def calculate_mean(total_sum, num_items):
#     return (total_sum) / (num_items)

# print(calculate_mean(total_sum,num_items))


# Question 3 - separate standalone file

# Question 4

groceries = [
    ["Baby Spinach", 2.78],
    ["Hot Chocolate", 3.70],
    ["Crackers", 2.10],
    ["Bacon", 9.00],
    ["Carrots", 0.56],
    ["Oranges", 3.08]
]


groceries = [
    ["Baby Spinach", 2.78],
    ["Hot Chocolate", 3.70],
    ["Crackers", 2.10],
    ["Bacon", 9.00],
    ["Carrots", 0.56],
    ["Oranges", 3.08],
]
def calculate_cost(unit_price, number_purchase):
    costs = []
    total_cost = 0
    for items in groceries:
        items_cost = float(unit_price) * int(number_purchase)
        costs.append(items_cost)
        total_cost += float(items_cost)
    print(costs)
    return f"${total_cost:.2f}"

for items in groceries:
    quantity = input(f"How many {items[0]} did you buy? ")
    price = items[1]

calculation = calculate_cost(price, quantity)
print(calculation)

print()

print("====Izzy's Food Emporium====")
for items in groceries:
    print(f"{items[0]:<17} ${items[1]:.2f}")
print("============================")
print(f"{calculation:>24}")
print()







# print(groceries)

# def calculate_cost(unit_price, number_purchase):
#     total_unit_cost = unit_price * number_purchase
#     return total_unit_cost


# total_unit_cost = 0

# for item in groceries:
#     item_quantity = input(f"How many units would you like of this item {item[0]}? ")
#     item.append(item_quantity)
#     item[1] = item[1] * int(item_quantity)
#     total_unit_cost += item[1]

# print(groceries)




    
#     item[1] = item[1] * int(item_quantity)
#     total += item[1]
   
# total = f"${total:.2f}"


# list1 = groceries


# for item in list1:
#     quantity = int(input(f"How many units would you like of this item {item[0]}? "))
#     item.append(quantity)
#     total_unit_cost = float(calculate_cost(item[1],quantity))
#     item.append(total_unit_cost)
# /

# for item in list1:
#     print(calculate_cost(unit_price, number_purchase))




# # print("====Izzy's Food Emporium====")
# # for items in list1:
# #     print(f"{item:<16} ${total_unit_cost:.2f}")
# #     print("============================")
# #     # print(f"{total_unit_cost:>25}")



# total_unit_cost = calculate_cost
# print(calculate_cost)


   
# total_units = f"${total_units:.2f}"


# unit_price = []
# for item in groceries:
#      print(f"${item[1]:7.2f}")









# number_purchase = []
# for item in groceries:
#     print




# print("====Izzy's Food Emporium====")
# for item in groceries:
#     print(f"{item[0]:<16} ${item[1]:7.2f}")
# print("============================")
# print(f"{total:>25}")