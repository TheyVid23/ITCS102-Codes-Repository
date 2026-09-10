
SenderName = input('What is your name? --> ')

TypeOfItem = input('What is your order? --> ')

is_Fragile = input('Is it fragile? (yes/no) --> ')

Weight = float(input('How heavy is it in kg? --> '))

Distance = float(input('How far is it from the designated destination in km? --> '))

is_Express = input('Is it in a hurry? (yes/no) --> ')

is_International = input('Is it from another country? (yes/no) --> ')

base_cost = (Weight * 2.5) + (Distance * 0.15)

if Distance <= 100 and Weight <= 2:
    Total = 0

elif is_International == 'yes' and is_Express == 'yes':
    Total = (base_cost * 1.4) + 50

elif Weight > 20 and is_International == 'yes' or is_Express == 'yes':
    Total = (base_cost * 1.2) + 25

elif Distance > 1000 and Weight > 30:
    Total = base_cost + 30

else:
    Total = base_cost

shippingfee = Total - base_cost


print()
print("DAVID'S EXPRESS")
print('Sender:', SenderName)
print('Order:', TypeOfItem)
print('Fragile:', is_Fragile)
print('Weight:', Weight, 'kg')
print('Distance:', Distance, 'km')
print('Express:', is_Express)
print('International:', is_International)
print('Base Cost: PHP', base_cost)
print('Shipping Fee: PHP', shippingfee)
print('Total: PHP', Total)



