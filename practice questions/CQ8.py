'''
8.Description:
Write a program to perform Addition, Subtraction, Multiplication and Division of 2 Numbers based on the user inputs by using Switch condition.(+ , - , * , /, %).

Constraints:
Input :      First line of input contains an Integer 

            Second line of input contains an Integer 

            Third line of Input Consists of Operator

Output :    Print Respective Output.

Constraints :  Operators Must accept only one of this Operators( +, -, *, /, % ) only.

Example:
Input  :     30 10 +
Output :   40 

Explanation:
NA

'''

# 1st way

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

operator = input("Enter the operator (+, -, *, /, %): ")
if operator == "+":
    print("The sum is:",a + b)
elif operator == "-":
    print("The difference is:",a - b)
elif operator == "*":
    print("The product is:",a * b)
elif operator == "/":
    print("The division is:",a / b)
elif operator == "%":
    print("The remainder is:",a % b)
else:
    print("Invalid Input")


# 2nd way

def math_operations():
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))
    operator = input("Enter operator: ")

    if operator == "+":
        print("The sum is:",a+b)
    elif operator == "-":
        print("The difference is:",a-b)
    elif operator == "*":
        print("The product is:",a*b)
    elif operator == "/":
        print("The division is:",a/b)
    elif operator == "%":
        print("The module is:",a%b)
    else:
        print("Invalid operator")

math_operations()

# 3rd way

def math_operator(a,b,operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b
    elif operator == "%":
        return a % b
    else:
        return "Invalid Input"

result = math_operator(300,100,"+")
print("The result is:",result)