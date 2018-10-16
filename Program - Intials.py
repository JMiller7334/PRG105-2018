def get_letters(string):
    to_return = []  # Initials will be stored in this list for simplicity.
    index = 0
    string = string.upper()  # All caps for initials thank you!
    to_return.append(string[0])  # first letter is always part of the initials.
    for char in string:
        index = index + 1
        if char == " ":
            to_return.append(string[index])  # we hit a space meaning next letter is part of the initials!
    return to_return


def main():
    print("Please use spaces between first, middle and last names. THANK YOU!")
    name = str(input("Please enter your first, middle, than last name "))
    initials = get_letters(name)
    if len(initials) > 2:
        print("Initials for " + str(name) + ". are " + initials[0] + ". " + initials[1] + ". " + initials[2] + ".")
    else:
        print("Error: only " + str(len(initials)) + " characters for initials were found. They are displayed below.")
        print(initials)  # what a shame...


main()
