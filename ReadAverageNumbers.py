def manage_data(file):
    entries = 0
    number_total = 0

    for line in file:
        entries = entries + 1
        stripped = line.strip()
        number_total = number_total + int(stripped)

    mean = number_total/entries
    mean = format(mean, ",.2f")
    number_total = format(number_total, ",")
    print("Total entries on file: " + str(entries))
    print("Total of all numbers on file: " + str(number_total))
    print("Average of numbers on file: " + str(mean))
    file.close()


def main():
    number_file = open("numbers.txt", "r")
    manage_data(number_file)


main()

