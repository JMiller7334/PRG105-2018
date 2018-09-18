# Notes included next to unfamiliar things so I can remind myself how I did it later.
days = int(input("Your Salary is $0.01 per day and doubles every day after. "
                 "Please enter how many days you want to check salary for. "))
total_salary = 0.00
total_pay = 0.00
runtime = 0

if days > 0:
    for runtime in range(0, days):
        if total_pay == 0.00:
            total_pay = 0.01
            # Print to table function below
            print(": Amount earned | Days worked :") # Prints the header for the table.
            table_pay = format(total_pay, ",.2f")
            table_pay = "$" + str(table_pay)

            table_day = runtime + 1 # Added 1 because runtime starts at 0. Thanks python.
            table_day = str(table_day)
            print(":" ,table_pay, " " * (12 - len(table_pay)), ":" ,table_day, " " * (10 - len(table_day)), ":") # The Magic!
        else:
            total_pay = total_pay * 2
            total_salary = total_salary + total_pay
            # Print to table function below
            print(": Amount earned | Days worked :")
            table_pay = format(total_pay, ",.2f")
            table_pay = "$" + str(table_pay)

            table_day = runtime + 1
            table_day = str(table_day)
            print(":" ,table_pay, " " * (12 - len(table_pay)), ":" ,table_day, " " * (10 - len(table_day)), ":")

            if runtime == (days - 1):
                print("Your total payout is: $" + format(total_salary, ",.2f"))
else:
    print("invalid number. Please re-run program and enter a valid number.")