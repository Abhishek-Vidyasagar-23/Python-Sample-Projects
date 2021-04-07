# 1. Star Pattern
print("****************** Star pattern****************")


def star_pattern(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("* ",end='')

        print()


n= 5
star_pattern(5)

# 2. Using List for star pattern

print("********** Star in list*****************")


def star_pattern_list(n):
    list = []
    for i in range(1,n+1):
        list.append("* "*i)
    print("\n".join(list))


star_pattern_list(5)

print("***************** 180 Degree Rotation*************")


def rotated_star_pyramid(n):

    k = 2*n-2

    for i in range(0,n):
        for j in range(0,k):
            print(end=" ")

        k= k-2
        for j in range(0,i+1):
            print("*",end=' ')
        print()


rotated_star_pyramid(5)

print("******************* Printing Whole triangle *************")


def full_triangle(n):
    k = n-1
    for i in range(0,n):

        for j in range(0,k):
            print(end=" ")

        k -= 1
        for j in range(0, i+1):
            print("*", end=' ')

        print()


full_triangle(10)

print("******************** Number Pattern without reassigning*************")


def repetitive_number_pattern(n):
    number= 1
    for i in range(0, n):
        number = 1
        for j in range(0, i+1):
            print(number, end=' ')

            number += 1
        print()


repetitive_number_pattern(5)

print("************************ Number Reassigned ****************")


def successive_number_pattern(n):
    number = 1
    for i in range(0, n):
        for j in range(0, i+1):
            print(number, end=" ")
            number += 1
        print()


successive_number_pattern(5)
