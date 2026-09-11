
SenderName = input('What is your name? --> ')

TypeOfItem = input('What is your order? --> ')

is_Fragile = bool(input('Is it fragile? (yes/no) --> ') == 'yes')

Weight = float(input('How heavy is it in kg? --> '))

Distance = float(input('How far is it from the designated destination in km? --> '))

is_Express = bool(input('Is it in a hurry? (yes/no) --> ') == 'yes')

is_International = bool(input('Is it from another country? (yes/no) --> ') == 'yes')

base_cost = (Weight * 2.5) + (Distance * 0.15)

if Distance <= 100 and Weight <= 2 and not is_Express and not is_International:
    Total = 0

elif is_International and is_Express:
    Total = (base_cost * 1.4) + 50

elif Weight > 20 and is_International or is_Express:
    Total = (base_cost * 1.2) + 25

elif Distance > 1000 or Weight > 30:
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



