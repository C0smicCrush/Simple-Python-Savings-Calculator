invval = 0#Savings starts out at 0
perc = 9 #9 is the annual SP rate of return on average since 1930
percSal = int(input("What percent do you expect your salary to increase annually?"))
percSav = int(input("What percent of your salary do you expect to put into your portfolio each year?"))
sal = int(input("What would your starting salary be?"))
years = int(input("How many years would you be working for?"))
for i in range(years):
    invval = invval*(1 + 9/100)#Savings natural appreciation
    invval = invval + sal*percSav/100#New amount added per year to savings
    sal = sal*(1 + percSal/100)#salary increase per year
invval = round(invval, 2)#Rounding so that we get value in cents
sal = round(sal,2)#Rounding so that we get value in cents
print("Savings Value after ", years, " years is $", invval)
print("\nSalary after ", years, " years is $", sal)
print("The expected income from this portfolio would be", round(invval*.04,2), "per year")
