code = 1

size = int(input("Enter size: "))

for i in range(1, size):
    for j in range(i):
        print(code, end=" ")
        code += 1
    print()