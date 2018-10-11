"""
    Complete all of the TODO directions 
    The number next to the TODO represents the chapter
    and section that explain the required code
    Your file should compile error free
    Submit your completed file
"""

# TODO 7.2 Lists
# Create a list of days of the week, assign it to the variable days, remove """ """ to test


days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Create a list with 5 items, set them all to 0, use the Repetition Operator ( * )
test_list = [0] * 5


# print the contents of your days list using the for operator
for day in days:
    print(day)


# print the list item that holds the value Saturday from the days list by using it's index
print(days[5])

# set the size variable to hold the length of the list days using the len function
size = len(days)

# concatenate the two following lists together, storing the value in list3 - remove the """ """ to test
list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]
list3 = list1 + list2
print(list3)

# TODO 7.3 List Slicing
# Slice the list days to select from Monday through Friday, inclusive, and assign the new list to work_days
# print work_days
new_list = days[0:5]
print(new_list)

# TODO 7.4 Finding items in Lists with the in Operator
# test to see if "Tue" is in the list days, print yes, Tue is in the list or no, Tue is not in the list
if "Tue" in days:
    print("yes, Tue is in list")
else:
    print("no Tue is not in list")

# TODO 7.5 List Methods and Useful Built-in Functions
# Complete the following code to append the last three months of the year to the list months. Remove
# the """   """ to test, and print the contents of months
months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept"]
months.append("Oct")
months.append("Nov")
months.append("Dec")
print("Months: ", months)

# get the index of "May" from the months list and print it on screen
print("The for index for May is " + str(months.index("May")))

# sort list3 from the 7.2 exercise and print the results on screen
list3.sort()
print("list3 sorted appears as: " + str(list3))

# reverse the order of list 3
list3.reverse()
print("list3 reversed appears as: " + str(list3))

# delete the number 5 from list 3
list3.remove(5)

# print the maximum item from list 3
print("Highest valued item in list3 is " + str(max(list3)))

# TODO 7.6 Copying Lists
# copy the list months to the variable months_of_the_year
# print the values in months_of_the_year
months_of_the_year = []  # method A (more work)
for entry in months:
    months_of_the_year.append(entry)
print(months_of_the_year)

months_of_the_year = [] + months  # Method B - stick to this much easier.
print(months_of_the_year)


# TODO 7.7 Processing lists
# total the values in list3 and print the results
total = 0
for num in list3:
    total = total + num
print("total of all item in list3: " + str(total))

# get the average of values in list 3 and print the results
total = 0
entries = 0
for number in list3:
    total = total + number
    entries = entries + 1
average = total/entries
average = format(average, ",.2f")
print("average of list3 is " + str(average))

# open the file states in read mode, read the contents of the file into the list states_list and print the
# contents of states_list on screen
file = open("states.txt", "r")
states_list = []
for line in file:
    new_line = line.strip()
    states_list.append(new_line)
print(states_list)
file.close()  #10/4/18 - added this. forgot to close file.

# TODO 7.8 Two-Dimensional Lists
# Create a two dimensional list that has the months of the year and the days in each month during a non leap year
# print the contents of the list
my_list = [["Jan", 31], ["Feb", 28], ["March", 31], ["April", 30]]
print(my_list)

# print just the values for index 3,0 and 3,1
print(my_list[3][0])
print(my_list[3][1])

# TODO 7.9 Tuples
# convert the months list to a tuple
my_tuple = tuple(months)

