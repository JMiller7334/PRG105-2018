def find_common(array, string):
    # Variables for first half (1st loop).
    matches = 0
    list_matches = []

    # Variables for 2nd half (2nd loop).
    last = 0
    count = 0
    index = 0  # This will be the index to return to. It will lead to the most used character.

    for element in array:  # build an array containing the # of times each letter was used.
        for child in array:
            if child == element:
                matches = matches + 1
        list_matches.append(matches)
        matches = 0

    for data in list_matches:  # filter data and determine the most used character.
        if int(data) > last:
            last = int(data)
            index = int(count)
        count = count + 1
    if last <= 1:  # in case there were no recurrences of any letters/numbers.
        print("There were no letters or numbers that occurred more than once in '" + str(string) + "'")
    else:
        print("The most used letter or number within '" + str(string) + "' is '" + str(array[index]) + "' recurring "
              + str(last) + " times.")


def main():
    phrase = str(input("This program will determine the number of matching letters and numbers within any phrase. "
                       "Please enter a phrase! "))
    print("\n")
    list_phrase = []
    string = phrase.upper()
    for char in string:  # builds an array containing only the letters/numbers used within the string.
        if char.isalpha() or char.isdigit():  # Filter out punctuation, spaces, etc.
            list_phrase.append(char)
    find_common(list_phrase, phrase)


main()
