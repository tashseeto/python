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
