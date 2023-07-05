'''
we will provide different outputs based on age
1 - 18 -> Important
21, 50, > 65 -> Important
All others -> Not Important
'''
# receive age and sotre it in a variable age
age = eval(input("Enter age: "))
# If age is both greater than one or equal to 1 and less than or eqaul to 18
# then we say Important
if (age >= 1) and (age <= 18):
    print("Important Birthday")

# if age is either 21 or 50 Important
elif (age == 21) or (age == 50):
    print("Important Birthday")

# we check if age is less than 65 and then convert true to fales and vice versa
elif not(age < 65):
    print("Important Birthday")

# else not Important
else:
    print("sorry not important birthday")
