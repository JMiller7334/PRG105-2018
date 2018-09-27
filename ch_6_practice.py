"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section that explain the required code
    Your file should compile error free
    Submit your completed file
"""

# TODO 6.1 Introduction to File Input and Output
# Assign the variable file_variable to open states.txt in read mode
file_variable = open('states.txt', 'r')

# Close the file
file_variable.close()

# Assign the variable state_capitals to open capitals.txt in write mode.
# Please note, the file does not currently exist, and by opening it in
# write mode you will create it
state_capitals = open('capitals.txt', 'w')
state_capitals.write("Phoenix, AZ\n")
state_capitals.write("Little Rock, AR\n")
state_capitals.write("Denver, CO\n")
state_capitals.close()

# Write three state capitals to the file
# There is a list of state capitals here: https://en.wikipedia.org/wiki/List_of_capitals_in_the_United_States
# sample
#   state_capitals.write("Alabama, Montgomery\n") - make sure to include the \n as a new line symbol
# close the file
# TODO reading data in from a file
# Assign the variable states_data to open states.txt in read mode
states_data = open("states.txt", "r")
# read in three lines from the file, assign to the variables below, Remove """   """ to test

line1 = states_data.readline()
line2 = states_data.readline()
line3 = states_data.readline()

# close the file
states_data.close()

# print the three variables
print(line1)
print(line2)
print(line3)

# TODO 6.2 Using loops to process files
# Complete the program below to read in and count all of the entries in the states file

# open the file in read mode

states_file = open("states.txt", "r")
counter = 0

# write a for loop to read in all of the lines, and print them on the screen, add 1 to counter for each line
for line in states_file:
    counter = counter + 1
    print(line)

# close the file
states_file.close()

# TODO 6.3 Processing records

# You are going to finish the program below to write data to a file

# entering book information
books = 3

# open the file books.txt for writing remove the """ """ to test
books_file = open("books.txt", "w")

# use a for loop to get title and author from the user use the range 1, books + 1

# get the data in the loop

for books in range(1, books + 1):
    title = str(input("please enter a book title "))
    author = str(input("please enter a book author "))
    books_file.write(str(title) + " by " + str(author) + "\n")

# write the data as a record in the loop, make sure to include the \n at the end of the line

# close the file
books_file.close()

# TODO 6.4 Exceptions
# In this exercise you will try to open a file that does not exist, capture the error,
# and display a custom error message

try:  # create a try statement:
    nil_file = open("superheros.txt", "r")
    nil_file.close()

# open the file superheros.txt for reading (we are not writing,
#  it would create the file)
# close the file

# create an except IOError, and a print statement telling the user that the file doesn't exist
except IOError:
    print("this file does not exist and cannot be read.")
