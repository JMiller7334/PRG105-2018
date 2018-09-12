"""
 Complete all of the TODO directions
 The number next to the TODO represents the chapter
 and section that explain the required code
 Your file should compile error free
 Submit your completed file
"""
# TODO 4.2 A condition controlled loop
# write a loop that will change the variable in num by subtracting 1
# then print the variable. Keep looping until the num = 0 (While num > 0)
# write your code here, the variable needs to exist before
# you test it
num = 10
while num > 0:
    print(num)
    num = num - 1

# TODO 4.3 the For Loop
# Use a for loop with a list of the days of the week, print each day
# of the week
week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
for day in week:
    print(day)
    if day == "Sunday":  # Maybe this isn't needed?
        break

# TODO 4.3 the for loop - range function
# use the range function to print the numbers from 1 to 10
for new_num in range(1, 11):  # Set to 11 to make it print to 10
    print(new_num)

# TODO 4.4 a running total
# Have the user enter 5 numbers, provide a total at the end
# You can assume integers
total = 0
for run_times in range(0, 5):
    user_num = int(input("Please enter a number"))
    total = total + user_num
    if run_times == 4:
        print(total)

# TODO 4.5 Sentinel Value
# Create a variable to store a total amount
# Create a variable to store a count of the numbers entered
# Have the user enter test scores until a sentinel value of -1 is
# entered.
# Display the total, the count and the average (total / count)

total_amount = 0
count = 0
entered = 0

while entered != -1:
    entered = int(input("Please enter test score, enter -1 to finish"))
    count = count + 1
    total_amount = total_amount + entered
    mean = total_amount / count
    print("Total:" + str(total_amount) + " Count:" + str(count) + " Mean:" + str(mean))

# TODO 4.6 validating data
# Ask the user to enter a number between 1 and 10.
# Use a while loop to force the user to repeat the
# prompt until the user enters a valid number. Test with
# both valid and invalid data

entered = int(input("Please enter a number between 1 and 10."))
while entered <= 0 or entered > 10:
    entered = int(input("Invalid number. Please enter a number BETWEEN 1 and 10, thank you!"))
