import getpass

username = 'userako'
password = 'davidmapagmahalx3d'

u = getpass.getpass('Input username --> ')
p = input('Input password --> ')

if username == u and p == password:
	print("ACCESS GRANTED")
else:
	print("ACCESS DENIED")