with open("./input/names/names.txt") as file:
    names_list = file.readlines()

with open("./input/letters/starting_letter.txt") as file:
    letter = file.read()
    for name in names_list:
        with open(f"./output/ready_to_send/{name}_letter.txt", "w") as file:
            custom_letter = letter.replace("[name]", name.strip())
            file.write(custom_letter)