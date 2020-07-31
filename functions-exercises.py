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

list1 = groceries

def calculate_cost(unit_price, number_purchase):
    total_unit_cost = unit_price * number_purchase
    return total_unit_cost

for item in list1:
    quantity = int(input(f"How many units would you like of this item {item[0]}? "))
    item.append(quantity)
    total_unit_cost = float(calculate_cost(item[1],quantity))
    item.append(total_unit_cost)

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
#     (f"{item[0]:<16} ${calculate_cost(unit_price, number_purchase):.2f}")
# print("============================")
# print(f"{total_:>25}")


# print("====Izzy's Food Emporium====")
# for item in groceries:
#     print(f"{item[0]:<16} ${item[1]:7.2f}")
# print("============================")
# print(f"{total:>25}")