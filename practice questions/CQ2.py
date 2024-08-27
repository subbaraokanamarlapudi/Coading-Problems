'''
2.Description:
Write a program to print all even numbers in range .if starting range is greater than ending range print "INVALID RANGE"

Constraints:
Input :               First line of input contains an Integer n represents starting range

                          Second line of input contains an Integer n1 represents ending range

Output :            Print All the Even Numbers in a Given Range.

 
Example:
Input :      1 10

output :   2 4 6 8 10

Explanation:
In the above example we have to print all the even numbers in the range of 1 to 10 with spaces
'''

# 1st-way

x = eval(input("Enter first number: "))
y = eval(input("Enter second number: "))

if x > y:
    print("Invalid Range")
else:
    even_numbers = []
    for i in range(x, y + 1):
        if i % 2 == 0:
            even_numbers.append(str(i))
    
    print(','.join(even_numbers))

# 2nd -way by using the normal function

def even_numbers(a,b):
    if a > b:
        print("Invalid Range")
    else:
        even_numbers = []
        for i in range(a, b + 1):
            if i % 2 == 0:
                even_numbers.append(str(i))
        print(','.join(even_numbers))

even_numbers(1,10)

#  3rd - way by using the user input

def even_numbers():
    x = eval(input("Enter first number: "))
    y = eval(input("Enter second number: "))
    if x > y:
        print("Invalid Range")
    else:
        even_numbers = []
        for i in range(x, y + 1):
            if i % 2 == 0:
                even_numbers.append(str(i))
        print(','.join(even_numbers))

even_numbers()