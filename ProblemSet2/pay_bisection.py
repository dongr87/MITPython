# use bisection method to calculate the minimum monthly payment to pay off in a year
def calc(balance, annualInterestRate):
    monthlyInterestRate = annualInterestRate/12.0
    low = balance/12.0
    high = (balance*(1+monthlyInterestRate)**12)/12.0
    payment = (low+high)/2.0
    tempBalance = balance

    for month in range(12):
        tempBalance = (tempBalance-payment) * (1+monthlyInterestRate)
        print  tempBalance
    while abs(tempBalance) > 0.01:
        if tempBalance > 0:
            low = payment
        else:
            high = payment
        payment = (high+low)/2.0
        tempBalance = balance
        for month in range(12):
            tempBalance = (tempBalance-payment) * (1+monthlyInterestRate)
    print 'Lowest Payment:', round(payment,2)

calc(320000,0.2)
calc(999999,0.18)
