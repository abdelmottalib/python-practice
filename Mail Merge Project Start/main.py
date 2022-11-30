# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# invited = open("./Input/Names/invited_names.txt")
with open("./Input/Letters/starting_letter.txt") as letter:
    read_letter = letter.read().rstrip()
with open("./Input/Names/invited_names.txt") as invited:
    for line in invited:
        with open(f"./Output/ReadyToSend/{line} letter.txt", "w") as file:
            letter_b = read_letter.replace("[name]", line.rstrip())
            file.write(letter_b)






