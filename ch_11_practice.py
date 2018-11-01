"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section that explain the required code
    Your file should compile error free
    Submit your completed file
"""


# TODO 11.1 Introduction to Inheritance
# You are going to create a Dwelling class based on the Automobile
# Sample from the chapter

# create the class Dwelling, the __init__ method should accept number_of_rooms, square_feet, floors
class Dwelling:
    def __init__(self, rooms, square_ft, floors):
        self.__rooms = rooms
        self.__square_ft = square_ft
        self.__floors = floors

    # add the mutators for all of the data attributes (number_of_rooms, square_feet, floors)
    def set_rooms(self, rooms):
        self.__rooms = rooms

    def set_square_ft(self, square_ft):
        self.__square_ft = square_ft

    def set_floors(self, floors):
        self.__floors = floors

    # add the accessors for all of  the data attributes
    def get_rooms(self):
        return self.__rooms

    def get_square_ft(self):
        return self.__square_ft

    def get_floors(self):
        return self.__floors


# Create the class Single_family_home as a sub class of Dwelling
# The __init__ method should accept number_of_rooms, square_feet, floors, garage_type, yard_size
class SingleFamilyHome(Dwelling):
    def __init__(self, rooms, square_ft, floors, garage_type, yard_size):
        # call the superclass of Dwelling and pass the required arguments, remember to include self
        Dwelling.__init__(self, rooms, square_ft, floors)
        # initialize the garage_type and yard_size attributes
        self.__garage_type = garage_type
        self.__yard_size = yard_size

    # create the mutator and accessor methods for the garage_type and yard_size attributes
    def set_garage_type(self, garage_type):
        self.__garage_type = garage_type

    def set_yard_size(self, yard_size):
        self.__yard_size = yard_size

    def get_garage_type(self):
        return self.__garage_type

    def get_yard_size(self):
        return self.__yard_size


# demonstrate the Single_family_home class, no need to import because you are in the same file

# create an object from the Single_family_home class with the following information:
# 6 rooms, 1200 square feet, 1 floor, single car garage, .25 acres
# Display the data using the accessor methods
new_home = SingleFamilyHome(6, 1200, 1, "single car", 0.25)


# create the main function
def main():
    print("New Home Info below")
    print("Number of Rooms : " + str(new_home.get_rooms()))
    print("Square Feet: " + str(new_home.get_square_ft()))
    print("Floors: " + str(new_home.get_floors()))
    print("Garage Type: " + str(new_home.get_garage_type()))
    print("Yard Acres: " + str(new_home.get_yard_size()))


# call the main function
main()


# TODO 11.2 Polymorphism
# Type in the mammal class from program 11-9    lines 1 - 22
class Mammal:
    def __init__(self, species):
        self.__species = species

    def show_species(self):
        print('I am a', self.__species)

    def make_sound(self):
        self.__species = self.__species   # <-- avoids formatting error.
        print("Grrrr")

    # create a Mouse class as a sub class of the mammal class following the Dog example


class Mouse(Mammal):
    def __init__(self):
        Mammal.__init__(self, "Mouse")

    def make_sound(self):
        print("whatever sound a mouse makes?")


# create a Bird class as a sub class of the mammal class following the Cat Example
class Bird(Mammal):
    def __init__(self):
        Mammal.__init__(self, "Bird")

    def make_sound(self):
        print("Chirp, chirp")


# Follow the example in program 11-10 (no need to import, use main2 instead of main
# because there is already a main on this page) use the Mouse and Bird class that you created
def main2():
    mouse = Mouse()
    mouse.show_species()
    mouse.make_sound()

    bird = Bird()
    bird.show_species()
    bird.make_sound()


main2()
