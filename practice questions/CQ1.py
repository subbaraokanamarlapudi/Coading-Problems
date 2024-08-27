'''
1. Description:
Write a program to print all numbers which are divisible by 11 in given range if no such numbers print NO NUMBERS if starting range is greater than ending range then print INVALID RANGE

Constraints:
Input :            First line of input contains an Integer n reperesent starting range

                       Second line of input contains an Integer n1 reperesent ending range

output :         all numbers which are divided by 11 in range

Example:
Input :       30 100

Output :     33 44 55 66 77 88 99


Explanation:
in the above example you have to print all 11 divisiors in range of 30 and 100

'''
# 1st-way

x = int(input("Enter a number: "))
y = int(input("Enter a number: "))

if x > y:
    print("Invalid Range")
else:
    for i in range(x,y):
        if i % 11 == 0:
            print(i,end=',')
        else:
            continue

# 2nd -way by using the normal function

def divisible_of_numbers(a,b):
    if a > b:
        print("Invalid Range")
    else:
        for i in range(a,b):
            if i % 11 == 0:
                print(i,end=',')
            else:
                continue
        print()

divisible_of_numbers(30,100)

#  3rd - way by using the user input

def divisible_of_numbers():

    a = eval(input("Enter first number: "))
    b = eval(input("Enter second number: "))
    
    if a > b:
        print("Invalid Range")
    else:
        for i in range(a,b):
            if i % 11 == 0:
                print(i,end=',')
            else:
                continue
        print()

# divisible_of_numbers(30,100)
divisible_of_numbers()