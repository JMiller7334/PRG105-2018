class OfficeFurniture:
    def __init__(self, category, material, length, width, height, price):
        self.__category = category
        self.__material = material
        self.__length = length
        self.__width = width
        self.__height = height
        self.__price = price

    def __str__(self):
        print("Type: " + str(self.__category) + " | Price: $" + str(self.__price) + " | Material: "
              + str(self.__material) + ".")
