'''
9.Description:
write a program to perform all these tasks

a.     Store a number in a variable

b.    If value is not in range (100-1000) prints WRONG NUMBER else follows the steps

c.     Check even or odd

d.    If even divide the number by 3 and print the remainder

e.     If odd divide the number by 2 and print the remainder.

Constraints:
Input : First line of input contains an Integer n reperesent number

Example:
Input :         498

Output :      0

Explanation:
in the above example number is in range of 100-1000 and it is even we are dividing with 3 and printing remainder 0

'''

# 1st way

n = int(input("Enter a number: "))  

if n in range(100, 1000):
    if n % 2 == 0:
        print(n % 3)  
    else:
        print(n % 2)  
else:
    print("WRONG NUMBER")

# 2nd way

def task_int():
    n = eval(input("Enter a number:"))

    if n in range(100, 1000):
        if n % 2 == 0:
            print(n % 3)
        else:
            print(n % 2)
    else:
        print("WRONG NUMBER")

task_int()

# 3rd way

def task_int(n):
    if n in range(100, 1000):
        if n % 2 == 0:
            return n % 3
        else:
            return n % 2
    else:
        return "WRONG NUMBER"

print(task_int(498))