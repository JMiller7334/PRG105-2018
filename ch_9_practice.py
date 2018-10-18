"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section that explain the required code
    Your file should compile error free
    Submit your completed file
"""
# TODO 9.1 Dictionaries
# Finish creating the following dictionary by adding three more people and birthdays
import pickle

birthdays = {'Meri': 'May 16',
             'Kathy': 'July 14',
             'Mikiya': 'Dec 20',
             'Touko': 'Aug 8',
             'Jacob': 'Dec 16'}

# Print Meri's Birthday
print(birthdays['Meri'])

# Create an empty dictionary named registration
registration = {}

# You will use the following dictionary for many of the remaining exercises

miles_ridden = {'June 1': 25, 'June 2': 20, 'June 3': 38, 'June 4': 12, 'June 5': 30, 'June 7': 25}

# print the keys and the values of miles_ridden using a for loop
for key in miles_ridden:
    print("Key: " + str(key) + " Value: " + str(miles_ridden.get(key)))

# get the value for June 3 and print it, if not found display 'Entry not found', replace the ""

value = miles_ridden.get("June 3")
if value is None:
    print('Entry not found')
else:
    print(value)
# get the value for June 6 and print it, if not found display 'Entry not found' replace the ""
value2 = miles_ridden.get('june 6')
if value2 is None:
    print('Entry not found.')
else:
    print(value2)

# Use the items method to print the miles_ridden dictionary
print(miles_ridden.items())


# Use the keys method to print all of the keys in miles_ridden
print(miles_ridden.keys())

# Use the pop method to remove june 4 then print the contents of the dictionary
miles_ridden.pop('June 4')
print(miles_ridden.keys())
print('\n')

# Use the values method to print the contents of the miles_ridden dictionary
print(miles_ridden.values())

# TODO 9.2 Sets
# Create an empty set named my_set
my_set = set()

# Create a set named days that contains the days of the week
my_set.add('mon')  # to avoid format error caused by: my_set = set([mon, etc])
my_set.add('tue')
my_set.add('wed')
my_set.add('thu')
my_set.add('fri')
my_set.add('sat')
my_set.add('sun')

# get the number of elements from the days set and print it
len(my_set)

# Remove Saturday and Sunday from the days set
my_set.remove('sat')
my_set.discard('sun')  # NOTE TO SELF: this does not raise an exception.
print(my_set)

# Determine if 'Mon' is in the days set
if 'mon' in my_set:
    print("monday is in this set.")

# TODO 9.3 Serializing Objects (Pickling)
# import the pickle library
# create the output file log and open it for binary writing
output_file = open('miles_ridden.dat', 'wb')  # NOTE TO SELF: wb for writing, rb for reading.

# pickle the miles_ridden dictionary and output it to the log file
pickle.dump(miles_ridden, output_file)

# close the log file
output_file.close()
