# print("Question 1")

# number = input("Please enter a number: ")

# total = 0
# count = 0
# while len(number) > 0:
#     count += 1
#     total += int(number)
#     number = input("Please enter another number: ")
# print(total)
# print(f"Your total is {total}.") - another output option irl - UX


# print("Question 2")

# mailing_list = [
#     ["Roary", "roary@moth.catchers"],
#     ["Remus", "remus@kapers.dog"],
#     ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
#     ["Biscuit", "biscuit@whippies.park"],
#     ["Rory", "rory@whippies.park"],
# ]

# for name in mailing_list:
#     print(f"{name[0]} : {name[1]}")


#  print("Question 3")

# my_list = []

# counter = 0
# while counter < 3:
#     counter += 1
#     user_prompt = input("Please enter a name: ")
#     my_list.append(user_prompt)  
# for user_prompt in my_list:
#     print(user_prompt)



print("Question 4")

groceries = [
    ["Baby Spinach", 2.78],
    ["Hot Chocolate", 3.70],
    ["Crackers", 2.10],
    ["Bacon", 9.00],
    ["Carrots", 0.56],
    ["Oranges", 3.08]
]

total = 0

for item in groceries:
    item_quantity = input(f"How many units would you like of this item {item[0]}? ")
    item[1] = item[1] * int(item_quantity)
    total += item[1]
   
total = f"${total:.2f}"

print("====Izzy's Food Emporium====")
for item in groceries:
    print(f"{item[0]:<16} ${item[1]:7.2f}")
print("============================")
print(f"{total:>25}")

