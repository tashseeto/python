is_raining = True

if is_raining:
        print("You'll need an umbrella today. ")



temperature = 17


if temperature <= 16:
    print("Take a jumper today.")
else:
    print("No need for a jumper today.")


is_cold = temperature < 16
is_hot = temperature > 2

print(is_cold, is_hot)

if is_cold:
    print("Take a jumper today.")
elif is_hot:
    print("Yuck, stay at home.")
else:
    print("Have a great day!.")

name = "Hayley"

if name == "Tash":
    print("You are awesome!")
else:
    print(f"Hi, {name}")