def make_list(file):
    array = []
    for line in file:
        line = line.strip()
        line = str(line).lower()
        array.append(line)
    return array


def main():
    boy_txt = open("BoyNames.txt", "r")
    girl_txt = open("GirlNames.txt", "r")

    boy_names = make_list(boy_txt)
    girl_names = make_list(girl_txt)
    boy_txt.close()
    girl_txt.close()

    name = str(input("Please enter a name. "))
    if name.lower() in boy_names:
        print(str(name) + " was one of the most popular boy names.")
    elif name.lower() in girl_names:
        print(str(name) + " was one of the most popular girl names.")
    else:
        print("This name was not popular among either gender.")


main()
