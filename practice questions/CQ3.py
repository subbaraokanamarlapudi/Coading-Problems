'''
3. Description:
Write a program to find sum of all the numbers in given range if starting index is greater than ending index print INVALID RANGE

Constraints:
Input :                First line of input contains integer n represent strating range

                           Second line of inputs contains integer n1 represent ending range

Output :            Print sum of numbers

Example:
Input :           10
                  20

Output :        165

Explanation:
print sum of all numbers in given range
'''

# 1st Way

x = eval(input("Enter first number: "))
y = eval(input("Enter second number: "))

if x > y:
    print("Invalid Range")
else:
    sum = 0
    for i in range(x, y + 1):
        sum = sum + i
    print(sum)

# 2nd Way by using the normal function

def sum_of_numbers(x, y):
    if x > y:
        print("Invalid Range")
    else:
        total = 0
        for i in range(x, y + 1):
            total += i
        return total
    
result = sum_of_numbers(10, 20)
print("The sum of numbers:",result)


# 3rd Way by using the lambda function

sum_of_numbers = lambda x, y: sum(range(x, y + 1)) if x < y else "Invalid Range"
result = sum_of_numbers(10, 20)
print("The sum of numbers:",result)

# lambda function by using user input

x = eval(input("Enter first number: "))
y = eval(input("Enter second number: "))

sum_of_numbers = lambda x, y: sum(range(x, y + 1)) if x < y else "Invalid Range"
result = sum_of_numbers(x, y)
print("The sum of numbers:",result)

# 4th Way by using the user input function

def sum_of_numbers():
    x = eval(input("Enter first number: "))
    y = eval(input("Enter second number: "))
    if x > y:
        print("Invalid Range")
    else:
        total = 0
        for i in range(x, y + 1):
            total += i
        return total
    
result = sum_of_numbers()
print("The sum of numbers:",result)