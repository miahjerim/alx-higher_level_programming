# ask the user to input miles and assign it to the miles variable
miles = input("Enter miles: ")
# Converty the the input from string to integer
miles = int(miles)
# convert miles to kilometers by multiplying 1.60934 times miles
kilometers = miles * 1.60934
# print the result using format()
print("{} miles eqauls {} kilometers".format(miles, kilometers))
