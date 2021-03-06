class PersonalProfile:
    def __init__(self):
        self.__name = "none"
        self.__address = "none"
        self.__age = 0
        self.__phone = "none"

    def set_name(self, new):
        self.__name = str(new)

    def set_address(self, new):
        self.__address = str(new)

    def set_age(self, new):
        self.__age = str(new)

    def set_phone(self, new):
        self.__phone = str(new)

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age

    def get_phone(self):
        return self.__phone


def main():
    jacob = PersonalProfile()
    jacob.set_age(24)
    jacob.set_name("Jacob Miller")
    jacob.set_address("1813 Home Drive")
    jacob.set_phone("815-555-8394")
    print("Name: " + jacob.get_name() + " | Age: " + str(jacob.get_age()) + " | Address: " + jacob.get_address() +
          " | Phone: " + jacob.get_phone())

    aj = PersonalProfile()
    aj.set_age(54)
    aj.set_name("AJ Miller")
    aj.set_address("1813 Home Drive")
    aj.set_phone("815-555-3446")
    print("Name: " + aj.get_name() + " | Age: " + str(aj.get_age()) + " | Address: " + aj.get_address() +
          " | Phone: " + aj.get_phone())

    gab = PersonalProfile()
    gab.set_age(27)
    gab.set_name("Gabrielle Miller")
    gab.set_address("7210 Somewhere Rd.")
    gab.set_phone("815-555-7842")
    print("Name: " + gab.get_name() + " | Age: " + str(gab.get_age()) + " | Address: " + gab.get_address() +
          " | Phone: " + gab.get_phone())


main()
