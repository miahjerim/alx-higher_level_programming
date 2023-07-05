'''
if the age is 5 then the person needs to be in kindergatten
age 6 through 17 goes to gades 1 through 12
if age is graeter than 17 say go to college
complete the code with 10 lines
'''
# ask the user to input age
age = eval(input("Enter Age: "))
grade = age - 5
suffix = ""
# Handle age being less than 5
if (age >= 0) and (age < 5):
    print("Under Age")
# Handle age 5 specialy
elif (age == 5):
    print("Go to Kindergarten")
# Handle age 6 to 17 for grade level
elif (age > 5) and (age <= 17):
    if (grade % 10 == 1) and (grade % 100 != 11):
        suffix = "st"
    elif (grade % 10 == 2) and (grade % 100 != 12):
        suffix = "nd"
    elif (grade % 10 == 3) and (grade % 100 != 13):
        suffix = "rd"
    else:
        suffix = "th"
    print("Go to {}{} grade".format(grade, suffix))

elif (age > 17) and (age <= 50):
    print("Go to college")

elif (age <= 0):
    print("Error please enter a valid Age")

else:
    print("Go Enjoy Life")
