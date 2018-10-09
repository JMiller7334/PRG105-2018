import random


def cal_list(table, answer):
    table.append(answer)
    table.sort()
    greatest = max(table)
    if greatest > answer:
        greater = table[int(table.index(answer)):20]
        greater.remove(answer)
        print("Numbers listed below are greater than the number you enter: " + str(answer))
        print(greater)
    else:
        print(str(answer) + " largest number available within the list. There are no numbers greater to display.")


def create_list():
    array = []
    count = 0
    for i in range(0, 20):
        count = count + 1
        rand = random.randint(1, 100)
        array.append(rand)
    # print("Debug: there are " + str(count) + " in list.")
    return array


def get_input():
    try:
        number = int(input("Please enter an integer between 1 and 100 "))
        if number <= 0:
            print("\n")
            print("Invalid number! Ensure number is higher than 0.")
        elif number >= 101:
            print("\n")
            print("Invalid number! Ensure number is less or equal to 100")
        else:
            # print("Debug: input is valid.")
            return number
    except ValueError:
        print("\n")
        print("Invalid number! Ensure number is an integer between 1 and 100.")


def main():
    table = create_list()
    answer = get_input()
    if answer is None:
        print("Program has stopped due to user error. Read above.")
    else:
        cal_list(table, answer)


main()
