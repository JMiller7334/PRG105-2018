# Running on a treadmill you burn 4.2 calories per minute.
# Write a program that uses a loop to display the number of calories burned after 10, 15, 20, 25 and 30 minutes.

runtime = 0
burned = 0

for runtime in range(0, 50):
    burned = runtime * 4.2

    if runtime == 10:
        print("In " + str(runtime) + "min you burned " + format(burned, ",.2f") + "Kcal")
    elif runtime == 15:
        print("In " + str(runtime) + "min you burned " + format(burned, ",.2f") + "Kcal")
    elif runtime == 20:
        print("In " + str(runtime) + "min you burned " + format(burned, ",.2f") + "Kcal")
    elif runtime == 25:
        print("In " + str(runtime) + "min you burned " + format(burned, ",.2f") + "Kcal")
    elif runtime == 30:
        print("In " + str(runtime) + "min you burned " + format(burned, ",.2f") + "Kcal")
        break