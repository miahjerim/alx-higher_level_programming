'''
Have the user enter their investment amount and expected interest
Each year their investment will increase by;
their investment + their investment * interest rates
we print out their earnings after 10yrs period
'''
# user enter investment
invest = input("How much are you investing? ")
itrst = input("what is your interest rate? ")

invest = float(invest)
itrst = float(itrst) * .01

for i in range(10):
    invest = invest + (invest * itrst)
print("10 years earnings : {:.2f}".format(invest))
# Handle 10yr period earning
