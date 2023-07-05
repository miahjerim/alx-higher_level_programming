# ASk the user to input 2 values and store them in variables num1 num2
num1, num2 = input('Enter 2 numbers ').split()

# convert the string into regular numbers integer
num1 = int(num1)
num2 = int(num2)

# Add the values entered and store them in sum
sum = num1 + num2
# Subtract the values and store them in difference
difference = num1 - num2

# Multily the values and store them in product
product = num1 * num2

# Divide the values and store them in quatient
quatient = num1 / num2

# Use modulus on the values to find the remainder
remainder = num1 % num2

# print the results
print("{} + {} = {}".format(num1, num2, sum))
print("{} - {} = {}".format(num1, num2, difference))
print("{} * {} = {}".format(num1, num2, product))
print("{} / {} = {}".format(num1, num2, quatient))
print("{} % {} = {}".format(num1, num2, remainder))
