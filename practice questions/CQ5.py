'''
5.Description:
Write a Program to Print the Biggest Number out of the Given three Numbers?

Constraints:
Input      :  Three integer values.

Output   :  Print the Biggest Number from the Given Numbers.

Example:

Input 1     :  25 69 819 

Output 1  :  819 is a Biggest Number from the Given Numbers

Input 2     :  100 222 212

Output 2  :  222 is a Biggest Number from the Given Numbers


Input 3    :  999 565  729

Output 3 :  999 is a Biggest Number from the Given Numbers

Explanation:
NA
'''

# 1st Way

x = eval(input("Enter first number: "))
y = eval(input("Enter second number: "))
z = eval(input("Enter third number: "))

if x > y and x > z:
    print(x, "is a Biggest Number from the Given Numbers")
elif y > x and y > z:
    print(y, "is a Biggest Number from the Given Numbers")
else:
    print(z, "is a Biggest Number from the Given Numbers")


# 2nd Way

def biggest_number(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

print(biggest_number(25,69,819))
print(biggest_number(100,222,212))
print(biggest_number(999,565,729))

# 3rd way

def biggest_number(a,b,c):
    return max(a,b,c)
print(biggest_number(25,69,819))
print(biggest_number(100,222,212))
print(biggest_number(999,565,729))

# 4th way

def biggest_number():
    a = eval(input("Enter first number: "))
    b = eval(input("Enter second number: "))
    c = eval(input("Enter third number: "))

    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

print(biggest_number())
print(biggest_number())
print(biggest_number())

