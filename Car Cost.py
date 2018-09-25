def yearly(cost):  # function gets total yearly cost and prints the final values to the user.
    year_cost = cost * 12  # calculates yearly total.

    year_cost = format(year_cost, ",.2f")  # formats the numbers
    cost = format(cost, ",.2f")

    print("You spend $" + str(cost) + " every month on your car.")
    print("Every year you spend a grand total of $" + str(year_cost) + " on your car.")


def monthly():  # functions gathers information from the user and returns this information to the main function.
    loan = float(input("How much is your monthly car loan? "))
    insur = float(input("How much do you spend on insurance every month? "))
    maint = float(input("How much do you spend on car maintenance every month? "))
    fuel = float(input("How much do you spend on fuel every month? "))

    total = loan + insur + maint + fuel  # Get monthly total.
    return total  # returns the total cost.


def main():
    month_cost = monthly()  # call said function.
    yearly(month_cost)

main()
