number = int(input("Enter the number of rows"))
shape = input("Enter the pattern")

for i in range(number):
    for j in range(i+1):
        print(shape, end='  ')

    print()
