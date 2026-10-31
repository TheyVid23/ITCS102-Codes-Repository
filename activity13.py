age = int(input("what is your age --> " ))

if age >= 1 and age <= 5:
	print("INFANT")

elif age >= 6 and age <= 12:
	print("KID")

elif age >= 13 and age <= 19:
	print("TEENAGER")

elif age >= 20 and age <= 29:
	print("EARLY ADULT")

elif age >= 30 and age <= 45:
	print("ADULT")

elif age >= 46 and age <= 59:
	print("LATE ADULT")

elif age >= 60 and age <= 150:
	print("SENIOR")

elif age >= 151:
	print("IMMORTAL")

else: 
	print("INVALID")