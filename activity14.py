age = int(input('What is your age? --> '))
is_employed = bool(input('Are you employed? (True/Leave blank if False) --> '))
credit_score = int(input('What is your credit score? --> '))
annual_income = float(input('What is your annual income? --> '))
has_collateral = bool(input('Do you have a collateral? (True/Leave blank if False) --> '))

base_interest = 0.0

if 60 > age >= 21 and is_employed == True:
    print('You pass the baseline criteria')
    if credit_score >= 750:
        print('You have a high credit score')
        if annual_income >= 100000:
            base_interest = 4.5
            print('You have a high salary and your final interst is ', base_interest)
        else:
            base_interest = 5.0
            print('You have an okay salary and your final interest is ', base_interest)
    elif 600 <= credit_score < 750:
        print('You have a fair credit')
        if has_collateral == True:
            base_interest = 7.0
            print('You have a collateral and your final interest is ', base_interest)
        elif annual_income < 40000:
            base_interest = 9.5
            print('You do not have a collateral and your income is bellow 40000, your final interest is ', base_interest)
    elif credit_score < 600:
        print('Rejected: Credit score too low')
else:
    print('Rejected: Fails baseline criteria')