tea_collection = ["Earl Grey", "Peppermint", "Lemon and Ginger", "Strawberry Cream"]
print(tea_collection)

print(tea_collection[0])
print(tea_collection[1])
print(tea_collection[0:2])
print(tea_collection[-1])
print(tea_collection[1:-1])
print(tea_collection[2:])


tea_collection[3] = "Melbourne Breakfast"
print(tea_collection)

print(len(tea_collection))
tea_collection.append("Chai")
print(tea_collection)
tea_collection.extend(["New York Breakfast", "Berry"])
print(tea_collection)
tea_collection.insert(2,"Rooibos")
print(tea_collection)

# # Removing from a list
# print()
# removed_tea = tea_collection.pop()
# print(removed_tea)
# tea_collection.pop(1)
# print(tea_collection)

# tea_collection.remove("Chai")
# print(tea_collection)

# del tea_collection[1:3]
# print(tea_collection)

# tea_collection.clear()
# print(tea_collection)

if len(tea_collection) <= 0:
    print("Oh no, I have run out of tea.")
else:
    print("Yay! I have tea!")


tea_collection.remove("Earl Grey")
tea_collection.remove("Chai")


if "Earl Grey" in tea_collection:
    print("I'll take an Earl Grey, please!")
elif "Chai" in tea_collection:
    print("I'll take a chai!")
else:
    print("Surprise me!")


tea_collection = [
    ["Earl Grey", "Melbourne Breakfast", "Chai"],
    ["Peppermint", "Lemon and Ginger", "Strawberry Cream"]
]

print(tea_collection)
print(tea_collection[0])
print(tea_collection[0][1])
print(tea_collection[1][-1])

tea_collection.append(["Chamomile", "Green", "Dandelion"])
print(tea_collection)

