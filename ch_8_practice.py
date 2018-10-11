"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section that explain the required code
    Your file should compile error free
    Submit your completed file
"""

# TODO 8.1 Basic string Operation
# Print all the characters from the name variable by accessing one character at a time
name = "John Jacob Jingleheimer Schmidt"
for letter in name:
    print(letter)

# Use the index to access and print the capital s in Schmidt from the variable name
print("\n")
print(name[24])

# Use the index with negative numbers to print the letters from the last name "Schmidt" in the
# name variable
print("\n")
print(name[-1])
print(name[-2])
print(name[-3])
print(name[-4])
print(name[-5])
print(name[-6])
print(name[-7])

# TODO 8.2 String slicing
# use string slicing to assign the middle name "Jacob" from name to the variable middle, replace the ""

middle = name[5:11]
print(middle)


# TODO 8.3 Testing, Searching, and manipulating strings
# test to see if the string "Jacob" is in name
search = "Jacob"
if search in name:
    print(str(search) + " is in " + str(name))

# test to see if the string "Michael" is in name
search = "Micheal"
if search in name:
    print(str(search) + " is in " + str(name))
else:
    print(str(search) + " is not in " + str(name))

# Test to see if name is a number
if name.isdigit():
    print(str(name) + " is a number.")
else:
    print(str(name) + "is not a number.")


# Test to see if number is a number
number = 42
if str(number).isdigit():
    print(str(number) + " is a number.")
else:
    print(str(number) + "is not a number.")


# Search for "J" in name, replace with "j" (lower case)
new_name = name.replace("J", "j")
print(new_name)

# split the string name into the variable name_list, replace the ""
name_list = [name[0:5], name[5:11], name[-7:-1]]  # Like so?
print(name_list)




