"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section that explain the required code
    Your file should compile error free
    Submit your completed file
"""

# TODO 3. 1 Relational Operators
# 1. Write a statement using the variables below and a
#   and a greater than sign that will evaluate to true.
# 2. Write a statement using the variables below that
#    compares two of the variables to see if they are equal
# 3. Write a statement using the variables below that compares
#    two of the variables below to see if they are not equal
# 4. Write a statement using the variables below that uses
#    the less than or equal to operator

# variables
a = 6
b = 8
c = 5

# 1
print(a > 3)  # returns true

# 2
print(a == b)

# 3
print(a != b)

# TODO 3.2 the if else statement
# add code below to determine if age is greater than or equal to
# 18. Depending on the answer, display the appropriate statement:
# "You are old enough to vote" or "You are not old enough to vote"
# Use the if-else structure

age = int(input("How old are you? "))
if age < 18:
    print("You are not old enough to vote.")
else:
    print("You are old enough to vote.")

# TODO 3.3 comparing strings
# complete the code below, if the user input matches the password
# string, display "that is correct" otherwise display "that is not
# correct"

password = "narwhals"
user_password = input("Please enter the password:  ")
if user_password == password:
    print("Password correct.")
else:
    print("password invalid.")

# TODO 3.4 if - elif - else
# write code that accepts a number from between 1 and 5 from the user
# and returns a roman numeral for that number. If the number entered is
# not between 1 and 5, have the else statement print "That is not a
# valid number"
user_number = input("Please enter a number between 1 and 5")
if user_number == 1:
    print("I")
elif user_number == 2:
    print("II")
elif user_number == 3:
    print("III")
elif user_number == 4:
    print("IV")
elif user_number == 5:
    print("V")
else:
    print("That is not valid number.")

# TODO 3.5 a series of conditions
# Buffet prices are based on the persons age. If the person is a senior
# citizen (62 or over) , the charge is $9.89. If the person is age 12-
# 61, the charge is $12.89. If it is a child of under age 3, they eat
# for free. If the child is between 4 and 12 they are charged $0.99 for
# each year of age. Complete the program below.

customer_age = int(input("How old is the customer?   "))
cost = 0  # initializing cost, assign the correct price to this variable

# complete the program here
if customer_age > 62:
    cost = 11.00
elif customer_age > 12:
    cost = 12.89
elif customer_age > 3:
    cost = int(customer_age) * .99
else:
    cost = 0
# output, correctly formatted:
print("Your cost for a customer who is " + str(customer_age) + " years old")
print("is $" + format(cost, ",.2f"))

# TODO 3.5 Logical Operators
# Using the variables below
# 1.) write a statement using the and operator that will evaluate to true
# 2.) write a statement using the or operator that will evaluate to true
# 3.) write a statement using the not operator that will evaluate to true

d = 10
e = 10
f = 12

print(d == e and e != f)

print(e > 3 or f > 17)

print(e != 3)

# TODO 3.6 Boolean variable
# You are programming a baby doll. If they baby doll is tired, it will close its eyes
# if it is hungry, it will cry. You will print  "Eyes open" or "Eyes closed" depending
# on the tired value. You will print "Crying" or "quiet" depending on the hungry variable

tired = True
hungry = False

if tired:
    print("Eyes closed")
else:
    print("Eyes open")
if hungry:
    print("Crying")
else:
    print("Quiet")
