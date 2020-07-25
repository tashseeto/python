print("Question 1")

number = input("Please enter a number: ")

total = 0
count = 0
while len(number) > 0:
    count += 1
    total += int(number)
    number = input("Please enter another number: ")
print(total)
# print(f"Your total is {total}.") - another output option irl - UX


