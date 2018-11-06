import ClassData


def main():
    print("\n")
    print("Please fill out information for the new employee.")
    name = str(input("Please enter the employee's name "))
    try:
        shift = int(input("Please enter " + str(name) + "'s shift number either 1, 2, or 3. "))
        if shift < 1 or shift > 3:
            print("Invalid shift entry. Shift must be an integer between 1 and 3.")
            main()
        else:
            number = int(input("Please enter " + str(name) + "'s employee number. Please ensure it is an integer. "))
            rate = float(input("Please enter " + str(name) + "'s hourly pay rate."))
            rate = format(rate, ",.2f")
            employee = ClassData.ProductionWorker(name, number, shift, rate)
            print("--- Employee Details Below ---")
            print("Employee Name: " + str(employee.get_employee_name()))
            print("Employee Number: " + str(employee.get_employee_number()))
            print("Employee Shift: " + str(employee.get_shift_number()))
            print("Hourly Pay Rate: $" + str(employee.get_hourly_pay_rate()))
    except ValueError:
        print("Invalid information entry. Please ensure information entered is in the correct format. Thank you!")
        main()


main()
