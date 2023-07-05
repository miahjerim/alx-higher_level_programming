# calculator
# store the user input of two numbers and operator
num1, operator, num2 = input('Enter Calculation ').split()
# convert the user input strings to interger except the operator
num1 = int(num1)
num2 = int(num2)
# if function to iterate and execute
if operator == "+":
    sum = num1 + num2
    print("{} + {} = {}".format(num1, num2, sum))
elif operator == "-":
    difference = num1 - num2
    print("{} - {} = {}".format(num1, num2, difference))
elif operator == "*":
    product = num1 * num2
    print("{} * {} = {}".format(num1, num2, product))
elif operator == "/":
    quatient = num1 / num2
    print("{} / {} = {}".format(num1, num2, quatient))
elif operator == "%":
    remainder = num1 % num2
    print("{} % {} = {}".format(num1, num2, remainder))
else:
    print("Error: operator not found")

# print the result
