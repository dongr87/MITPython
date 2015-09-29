def calc(balance, annualInterestRate):
    monthlyInterestRate = annualInterestRate/12.0
    payment = 0
    tempBalance = 1
    while tempBalance > 0:
        payment += 10
        tempBalance = balance
        for month in range(12):
            tempBalance = (tempBalance - payment)*(1+monthlyInterestRate)
    print 'Lowest Payment:', payment

calc(3329, 0.2)
calc(4773, 0.2)
calc(3926, 0.2)

