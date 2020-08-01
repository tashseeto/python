# Question 1

groceries = {
"Baby Spinach": 2.78,
"Hot Chocolate": 3.70,
"Crackers": 2.10,
"Facon": 9.00,
"Carrots": 0.56,
"Oranges": 3.08
}

for item in groceries:
    print(item, groceries[item])

def calculate_cost(unit_price, number_purchase):
    total_unit_cost = unit_price * number_purchase
    return total_unit_cost

total = 0

for item in groceries:
    item_quantity = input(f"How many units would you like of this item {item}? ")
    groceries[item] = calculate_cost(groceries[item],int(item_quantity))
    total += groceries[item]

total = f"${total:.2f}"

print("====Izzy's Food Emporium====")
for item in groceries:
    print(f"{item:<16} ${groceries[item]:7.2f}")
print("============================")
print(f"{total:>25}")

