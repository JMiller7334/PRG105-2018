import Class
import SubClass


def main():
    print("----- Furniture Listing Below -----")
    furniture = Class.OfficeFurniture("Table", "Wood", 64, 32, 32, 100.00)
    furniture.__str__()

    furniture = SubClass.Desk("Desk", "Fancy", 38, 38, 32, 250.00, "Left Side", 3)
    furniture.__str__()


main()
