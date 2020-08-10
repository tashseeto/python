names = []

with open("names.txt") as txt_file:
    # print(txt_file)
    for line in txt_file:
        line = line.strip()
        # the immediate code above removes the \n (new line character)
        names.append(line)

print(names)


for name in names:
    print(name)


with open("names_output.txt", "w") as txt_file:
    for name in names:
        txt_file.write(name + "\n")
        # the immediate code above adds a new line space "\n" - otherwise will write all in one line
        



  