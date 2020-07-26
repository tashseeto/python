names = []

with open("names.txt") as txt_file:
    for line in txt_file:
        line = line.strip()
        names.append(line)

    for counter, name in enumerate(names, 1):
            print(f"{counter}.  {name}")
     

