years = int(input("Please enter how many years you want to check rainfall for." ))
year = 0
runtime = 0
total = 0

for runtime in range(0, years):
    for month in ("January", "Febuary", "march", "April", "May", "June", "July", "August", "September", "October",
                  "November", "December"): # Much easier this way
        year = runtime + 1 # Python starts at 0...
        if month == "January":
            print("rainfall for year " + str(year))
        inches = float(input("Please enter how many inches of rainfall for " + str(month) + " for year " + str(year)))
        total = total + inches

print("Total rainfall for " + str(years) + " years is " + format(total, ",.2f") + ".")
mean = total/(years * 12)
print("Mean rainfall for " + str(years) + " is " + format(mean, ",.2f") + ".")