# This program translates phone numbers that have letters in them. It accepts phone numbers with and without dashes and
#  or spaces. It also accepts phone numbers that do include 1 before the area code e.i 800-GET-FOOD.


def translate_number(number):
    translated_number = []
    number_list = []
    number_key = {"2": ["A", "B", "C"],
                  "3": ["D", "E", "F"],
                  "4": ["G", "H", "I"],
                  "5": ["J", "K", "L"],
                  "6": ["M", "N", "O"],
                  "7": ["P", "Q", "R", "S"],
                  "8": ["T", "U", "V"],
                  "9": ["W", "X", "Y", "Z"]}

    for char in number:
        if char.isdigit() or char.isalpha():
            number_list.append(char)
    if len(number_list) < 10:
        print("Error: phone number that was entered was not 10 digits long.")
    else:
        for digit in number_list:
            for key, value in number_key.items():
                for list_item in value:
                    if list_item == digit.upper():
                        translated_number.append(key)

        converted_list = number_list[0:-(len(translated_number))] + translated_number
        return converted_list


def main():
    print("This program translates phone numbers that have words within them. Ie. 1-800-GET-FOOD")
    phone_number = str(input("Please enter the phone # to translate. "))
    t = translate_number(phone_number)
    print("The translated number is listed below for " + str(phone_number))
    if len(t) > 10:
        seg_1 = ''.join(map(str, t[1:4]))
        seg_2 = ''.join(map(str, t[4:7]))
        seg_3 = ''.join(map(str, t[7:12]))
        print(str(t[0]) + "-" + str(seg_1) + "-" + str(seg_2) + "-" + str(seg_3))
    else:
        seg_1 = ''.join(map(str, t[0:3]))
        seg_2 = ''.join(map(str, t[3:6]))
        seg_3 = ''.join(map(str, t[6:11]))
        print(str(seg_1) + "-" + str(seg_2) + "-" + str(seg_3))


main()
