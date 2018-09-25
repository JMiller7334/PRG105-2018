def calc_carb():  # Gets user input and calculates total total carbs. returns calculated value.
    grams = int(input("How many grams of carbs did you eat today? "))
    total = grams * 4
    return total


def calc_protein():  # Gets user input and calculates total total protein. returns calculated value.
    grams = int(input("How many grams of carbs did you eat today? "))
    total = grams * 4
    return total


def calc_fat():  # Gets user input and calculates total total fatss. returns calculated value.
    grams = int(input("How many grams of carbs did you eat today? "))
    total = grams * 9
    return total

def main():  # call the other 3 functions, generates a grand total, and prints results to the user.
    carb = calc_carb()
    protein = calc_protein()
    fat = calc_fat()

    total = carb + protein + fat
    print("today you ate a total of " + str(total) + "kcal")


main()