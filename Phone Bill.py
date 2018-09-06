print("Listed below are the 3 plans we offer.")
print("Package A: For $39.99 per month 450 minutes are provided. Additional minutes are $0.45 per minute.")
print("Package B: For $59.99 per month 900 minutes are provided. Additional minutes are $0.40 per minute.")
print("Package C: For $69.99 per month unlimited minutes provided.")

plan = str(input("Please choose either A, B or C to indicate your plan. "))
plan_lower = plan.lower()

minutes = int(input("Thank you! Now please enter the number of minutes used. "))
used = 0  # placeholder so I do not lose the users original input
Cost = 0.00

if plan_lower == "a":
    used = minutes - 450
    if used <= 0:
        print("You used " + str(minutes) + " minute(s). You owe $39.99.")
    else:
        cost = (used * 0.45)
        cost = cost + 39.99
        cost = format(cost, ',.2f')
        # cost = str(cost)
        print('You used', minutes, 'minutes. you owe $' + str(cost) + '.')

elif plan_lower == "b":
    used = minutes - 900
    if used <= 0:
        print("You used " + str(minutes) + " minute(s). you owe $59.99.")
    else:
        cost = (used * 0.40)
        cost = cost + 59.99
        cost = format(cost, ',.2f')
        # cost = str(cost)
        print("You used " + str(minutes) + " minutes. you owe $" + str(cost) + ".")
elif plan_lower == "c":
    print("you have unlimited minutes. Your monthly bill is $69.99.")
else:
    print("Invalid plan entered. Please enter only A, B, or C to indicate your plan. Please run program again.")
