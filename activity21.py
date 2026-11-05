sum = 0
tuloy = True
tries = 3

while tuloy == True and tries > 0:
    x = int(input("Enter a number --> "))

    if x == 0:
        print("LOOP TERMINATED")
        print(f"Your total is {sum}")
        break

    else:
        print("LOOP CONTINUE")
        sum += x
        print(f"Your current total is {sum}")
        tries = tries - 1
        print(f"Your current tries is {tries}")
        continue