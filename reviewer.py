owner_age = int(input('What is your age? --> '))
monthly_revenue = float(input('How much is your monthly revenue? --> '))
credit_score = int(input('What is your credit score? --> '))
years_in_business = float(input('How long is your business running? --> '))
has_defaults = bool(input('Did you file for bankruptcy? --> '))
collateral_name = input('What is your collateral? --> ')
collateral_value = float(input('How much is the value of your collateral? --> '))

max_loan = 0.0
base_fee_rate = 0.0

if owner_age >= 21 and years_in_business >= 2 and has_defaults == False:
    print('YOU PASSED THE BASELINE REQUIREMENTS')
    if credit_score >= 720:
        max_loan = monthly_revenue * 3
        print ('YOU HAVE A MAX LOAN OF', max_loan)
        if monthly_revenue >= 50000:           
            base_fee_rate = max_loan * 0.015
            print('YOU HAVE A BASE FEE RATE OF', base_fee_rate)
        else:
            base_fee_rate = max_loan * 0.025
            print('YOU HAVE A BASE FEE RATE OF', base_fee_rate)

        if collateral_value >= max_loan:
            print('YOUR COLLATERAL VALUE IS GREATER THAN YOUR MAX LOAN')
        else:
            print('Rejected: Insufficient collateral value for', collateral_name)

        surcharge_fee_rate = base_fee_rate * max_loan
        if int(collateral_value) % 5000 != 0:
            print('YOU WILL HAVE AN ADDITIONAL FEE')
            surcharge_fee_rate += 250
            print(' YOUR ADDED FEE IS', surcharge_fee_rate)

    elif 620 <= credit_score < 720:
        max_loan = monthly_revenue * 1.5
        print ('YOU HAVE A MAX LOAN OF', max_loan)
        if years_in_business >= 5:
            base_fee_rate = max_loan * 0.02
            print('YOU HAVE A BASE FEE RATE OF', base_fee_rate)
        else:
            base_fee_rate = max_loan * 0.035
            print('YOU HAVE A BASE FEE RATE OF', base_fee_rate)

        if collateral_value >= max_loan:
            print('YOUR COLLATERAL VALUE IS GREATER THAN YOUR MAX LOAN')
        else:
            print('Rejected: Insufficient collateral value for', collateral_name)

        surcharge_fee_rate = base_fee_rate * max_loan
        if int(collateral_value) % 5000 != 0:
            print('YOU WILL HAVE AN ADDITIONAL FEE')
            surcharge_fee_rate += 250
            print('YOUR ADDED FEE IS', surcharge_fee_rate)

    elif credit_score < 620:
        print('YOUR CREDIT SCORE IS TOO LOW')

    else:
        print('INVALID ')             
else:
    print('YOU DID NOT PASS THE BASELINE REQUIREMENTS')