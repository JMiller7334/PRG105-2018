import Class


class Desk(Class.OfficeFurniture):
    def __init__(self, category, material, length, width, height, price, drawer_location, drawer_number):
        Class.OfficeFurniture.__init__(self, category, material, length, width, height, price)

        self.__category = category
        self.__material = material
        self.__length = length
        self.__width = width
        self.__height = height
        self.__price = price

        self.__drawer_location = drawer_location
        self.__drawer_number = drawer_number

    def __str__(self):
        print("Type: " + str(self.__category) + " | Price: $" + str(self.__price) + " | Drawer Location: "
              + str(self.__drawer_location) + " | Total Drawers: " + str(self.__drawer_number) + "")

