def create_message(first_name, last_name):
    # a = 1
    print(f"Hi {first_name} {last_name}!")

create_message("Tash", "Seeto")

# create_message("Tash")
# create_message("Tabitha")
# create_message("Hayley")

# person = "Tash"
# create_message(person)

# name = "ducks"
# print(name)
# print(a)

def is_even(number):
    if number%2 == 0:
        return True
    else:
        return False

num2 = is_even(2)
num3 = is_even(5)

print(num2, num3)


counter = 5
while counter > 0:
    if is_even(counter):
        print(f"{counter} is an even number.")
    else:
        print(f"{counter} is an odd number.")
    counter -= 1


# Hayleys example
def awesome_message(name):
    return f"{name} is awesome!"
def generic_greeting(name):
    return f"Hi, {name}"

name = input("What is your name? ")
if name == "Hayley":
    print(awesome_message(name))
else:
    print(generic_greeting(name))


