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

my_list = []

counter = 0
while counter < 3:
    counter += 1
    user_prompt = input("Please enter a name: ")
    my_list.append(user_prompt)  
print(my_list)

