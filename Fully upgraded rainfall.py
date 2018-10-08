# This program will track all matching rainfall entries and corresponding months. When finished it will tell you of
# each month that had matching amounts of rainfall along with the amount of rainfall these months had in common.
# furthermore it will give the total, max, min, and average of rainfall for the year too as well as the months that had
# min/max rainfall in common. Those months will be listed together.

month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
month_rainfall = []  # Holds individual rainfall entries.
month_match = []  # Holds the names of matching months with common rainfall.
existing = []  # Used to keep track of existing matching rainfall entries (inches).


def get_index(array, value):  # function used to locate the index within lists. BUT THERE MUST BE AN EASIER WAY!?
    index = 0
    for search in array:  # note to self: 'search' is variable being looked for within the list.
        index = index + 1
        if search == value:
            return index


def main():
    total = 0  # total overall rainfall.
    matching = 0  # total number of matching rainfall entries.
    print("\n")
    for month in month_names:
        rainfall = float(input("Please enter in inches the amount of rainfall for " + str(month) + ". "))

        if rainfall in month_rainfall:
            if rainfall in existing:  # below updates existing matching entry[adds new month name.]
                month_match[existing.index(rainfall)].append(str(month))  # array - existing supplies the correct index!
            else:  # below creates a new matching entry since no entry was found.
                month_match.append([])
                prev_month = get_index(month_rainfall, rainfall)  # Find the index for name of previous month with same
                # rainfall entry.
                month_match[matching].append(str(month_names[int(prev_month) - 1]))  # Adds previous month name to list.
                month_match[matching].append(str(month))  # Adds current month name to matching lst.
                matching = matching + 1
                existing.append(float(rainfall))

        month_rainfall.append(float(rainfall))
        total = total + rainfall

    mean = total / 12

    rainfall_max = max(month_rainfall)
    max_index = get_index(month_rainfall, rainfall_max)
    max_name = month_names[max_index - 1]

    rainfall_min = min(month_rainfall)
    min_index = get_index(month_rainfall, rainfall_min)
    min_name = month_names[min_index]
    print("\n")
    if rainfall_max in existing:
        temp_index = existing.index(rainfall_max)
        print("Months listed below had the most amount of rainfall they had " + str(existing[temp_index]) + " inches.")
        print(month_match[temp_index])
    else:
        print("Month with the highest rainfall is " + str(max_name) + " at " + format(rainfall_max, ",.2f") +
              str(" inches"))

    if rainfall_min in existing:
        temp_index = existing.index(rainfall_min)
        print("Months listed below had the least amount of rainfall they had " + str(existing[temp_index]) + " inches.")
        print(month_match[temp_index])
    else:
        print("Month with the lowest rainfall is " + str(min_name) + " at " + format(rainfall_min, ",.2f") + str(
            "inches"))

    print("Average rainfall for the year is " + format(mean, ",.2f") + " inches.")
    print("Total Rainfall for the year is " + format(total, ",.2f") + " inches.")
    if matching > 0:
        print("\n")
        for i in range(0, matching):
            current = month_match[int(i)]
            print("Months with " + str(existing[int(i)]) + " inches are listed below.")
            print(current)


main()
