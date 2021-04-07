# create a function

def pyramid(n):  # n is the number of desired rows
    number = 1  # initialise the first number
    for i in range(0, n):
        for j in range(0, i+1):
            print(number, end=' ')
            number = number+1 # increment the number
        print()


n = 5
pyramid(n)
