for x in range(10, 0, -1):
    for y in range(1,  x):
            print("*", end=" ")
    print("*")
for x in range(1, 11):
    for y in range(1,  x):
            print(x, end=" ")
    print(x)

# for x in range(10, 0, -1):
#     print(" ".join("*" for _ in range(x)))

# for x in range(1, 11):
#     print(" ".join(str(y) for y in range(1, x + 1)))

#The comment part is just an additional way of doing it. 
