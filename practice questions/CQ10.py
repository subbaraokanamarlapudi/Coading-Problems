'''
10.Description:
Write a program to convert temperature from degree celcisu (C) to Farenheit (F).

Constraints:
Input           :    First line of input contains Integer 'n' represents temperature in celcius

Output         :   Temperature in farenheit

Example:
Input     :   96

Output  :   204.8F

Explanation:
In the above example input is 96,now you have to convert it into farenheit 

if we convert the value of 96 to farenheit we will get 204.8

note:  f=(c*9/5)+32

'''

# 1st way

n = int(input("Enter temperature in celcius: "))
f = (n*9/5)+32
print(f"{f}F")

# 2nd way

def celcius_to_fahrenheit(n):
    return (n * 9/5) + 32

result = celcius_to_fahrenheit(96)
print(f"{result}F")

# 3rd way
def celcius_to_fahrenheit():
    n = int(input("Enter temperature in celcius: "))
    return (n * 9/5) + 32

result = celcius_to_fahrenheit()
print(f"{result}F")

# 4th way ----> Fahrenhit to Celcius

n = eval(input("Enter temperature Farenheit:"))
c = (n-32)*5/9
# print(f"{c}C")
# print(f"{c:.2f}C") # round to 2 decimal places
print(c)

# 5th way

def fahrenheit_to_celcius(n):
    return (n-32)*5/9
result = fahrenheit_to_celcius(204.8)
print(f"{result}C")

# 6th way
def celcius_to_fahrenheit():
    n = eval(input("Enter temperature in celcius: "))
    return (n-32)*5/9

result = celcius_to_fahrenheit()
print(f"{result}C")