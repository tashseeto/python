# while loops are for doing something until a condition is no longer met

counter = 10

while counter > 0:
    print(counter)
    # counter -= 1 - shorthand for the below
    counter = counter - 1

    while counter > 0:
        print(counter)
        if counter%2 == 0:
            print(f"{counter} is an even number.")
        else:
            print(f"{counter} is an odd number.")
        counter -=1

count = 0
while count < 3:
    name = input("What is your name? ")
    if name == "Vivian":
        print("You are awesome!")
    else:
        print(f"Hi, {name}.")
    count += 1

# the below will continue forever
name = input("What is your name? ")
while len(name) > 1:
    if name == "Vivian":
        print("You are awesome!")
    else:
        print(f"Hi, {name}.")
    name = input("What is your name? ")

