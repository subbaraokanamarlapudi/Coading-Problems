'''
7.Description:
Write a program to print Full Stack Python for 'N' times

Constraints:
Input :              One Integer Value Consists in First Line of Input.

Output :           Print Full Stack Python for 'N' Times.

Constraints :    10<N<100

Example:
Input 1 :      11

Output 1 :

Full Stack Python
Full Stack Python
Full Stack Python
Full Stack Python
Full Stack Python
Full Stack Python
Full Stack Python
Full Stack Python
Full Stack Python
Full Stack Python
Full Stack Python

Input 2 :      111

Output 2 :   Invalid Input

Explanation:
NA
'''

# 1st way

n = int(input("Enter the number: "))

if n > 10 and n < 100:
    for i in range(n):
        print("Full Stack Python")
else:
    print("Invalid Input")

# 2nd way
def how_many_times(n):
    if n > 10 and n < 100:
        for i in range(n):
            print("Full Stack Python")
    else:
        print("Invalid Input")

how_many_times(11)
how_many_times(111)