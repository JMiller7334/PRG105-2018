# Cookie calculator!!
cookies = float(input("Enter the number cookies you want to make "))
sugar = cookies * 0.03125
flour = cookies * 0.02083
butter = cookies * 0.05729

sugar = format(sugar, ',.2f')
flour = format(flour, ',.2f')
butter = format(butter, ',.2f')

str_sugar = str(sugar)
str_butter = str(butter)
str_flour = str(flour)
str_cookies = str(cookies)

print("For " + str_cookies + " cookies you need the following")
print(str_sugar + " cups of sugar")
print(str_flour + " cups of flour")
print(str_butter + " cups of butter")
