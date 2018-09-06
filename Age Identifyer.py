age = int(input("Please enter your age. "))
if age < 1:
    print("Infant")
elif age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
else:
    print("Adult")
