print("Question 1")

moths_in_house = True

if moths_in_house:
    print("Get the moths!")

moths_in_house = False

if not moths_in_house:
    print("No threats detected.")


print("Question 2")

moths_in_house = True
mitch_is_home = True

if moths_in_house and mitch_is_home:
    print("Hooman! Help me get the moths!")

moths_in_house = False
mitch_is_home = False

if not moths_in_house and not mitch_is_home:
    print("No threats detected.")

moths_in_house = True
mitch_is_home = False

if moths_in_house and not mitch_is_home:
    print("Meoooooooooooooooww! Hisssssss!")

moths_in_house = False
mitch_is_home = True

if not moths_in_house and mitch_is_home:
    print("Climb on Mitch.")

print("Question 3")

light_colour = "Red"
car_detected = False

if light_colour and not car_detected:
    print("Do nothing.")

light_colour = "Red"
car_detected = True

if light_colour and car_detected:
    print("Flash!")

light_colour = "Green"
car_detected = False

if light_colour and not car_detected:
    print("Do nothing.")

light_colour = "Green"
car_detected = True

if light_colour and car_detected:
    print("Do nothing.")

light_colour = "Amber"
car_detected = False

if light_colour and not car_detected:
    print("Do nothing.")

light_colour = "Amber"
car_detected = True

if light_colour and car_detected:
    print("Do nothing.")

print("Question 4")

height_required = 119
height_prompt = input("How tall are you in cm?: ")
height_prompt = int(height_prompt)

if height_prompt > height_required:
    print("Hop on!")
else:
    print("Sorry, not today!")