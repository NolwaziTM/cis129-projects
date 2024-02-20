# Module 04- lab 04
#Author- Nolwazi Moyo
# Date 02/19/2024

monthlySales = 0  # amount for monthly sales
storeAmount = 0   #store bonus 
empAmount = 0  # employee bonus
salesIncrease = 0 #percentage of sales increase
prompt = ("Enter the monthly sales amount:") # string literal

#code for the monthly sales
monthlySales = float(input("Enter the monthly sales:"))

#code that determines the store bonus
if monthlySales >= 110000:
    storeAmount = 6000
elif monthlySales >= 100000:
    storeAmount =  5000
elif monthlySales >= 90000:
    storeAmount = 4000
elif monthlySales >= 80000:
    storeAmount = 3000
else:
    storeAmount = 0


#code for the percentage increase in sales
salesIncrease = float(input("Enter the percentage increase in salses:"))
salesIncrease = salesIncrease / 100

#code determining the employee bonus
if salesIncrease >= .05:
    empAmount =75
elif salesIncrease >= .04:
    empAmount = 50
elif salesIncrease >= .03:
    empAmount = 40
else:
    empAmount = 0


# This code outputs the bonus information
print ("The store bonus amount is $", storeAmount)
print("The employee bonus amount is $", empAmount)
if storeAmount == 6000 and empAmount == 75:
    print('Congrats! You have reached the highest bonus amounts possible!')