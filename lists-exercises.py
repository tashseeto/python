# # print("Question 1")

# # foods = ["orange", "apple", "banana", "strawberry", "grape", "blueberry",["carrot", "cauliflower", "pumpkin"], "passionfruit", "mango", "kiwifruit"]

# # print(foods)

# # print(foods[0])
# # print(foods[2])
# # print(foods[-1])
# # print(foods[0:3])
# # print(foods[7:])
# # # print(foods [-3:]) - alternate to above
# # print(foods[6][2])


# print("Question 2")

# mailing_list = [
#     ["Roary", "roary@moth.catchers"],
#     ["Remus", "remus@kapers.dog"],
#     ["Prince Thomas of Whitepaw", "hrh.thomas@royalty.wp"],
#     ["Biscuit", "biscuit@whippies.park"],
#     ["Rory", "rory@hippies.park"],
# ]

# print(mailing_list)
# print(f"{mailing_list[0][0]} : {mailing_list[0][1]}")
# print(f"{mailing_list[1][0]} : {mailing_list[1][1]}")
# print(f"{mailing_list[2][0]} : {mailing_list[2][1]}")
# print(f"{mailing_list[3][0]} : {mailing_list[3][1]}")
# print(f"{mailing_list[4][0]} : {mailing_list[4][1]}")


print("Question 3")

names = ["James", "Tom", "Luke"]
print(names)

nameA = input("Please provide a name: ")
nameB = input("Please provide a name: ")
nameC = input("Please provide a name: ")

names.append("(input(nameA)")
names.append(input(nameB))
names.append(input(nameC))

print(names)