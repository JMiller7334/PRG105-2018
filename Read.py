def read_names(file):
    counter = 0
    for line in file:
        counter = counter + 1
        print(line)
    print("total names in file: " + str(counter))


def main():
    names_file = open("names.txt", "r")
    read_names(names_file)


main()
