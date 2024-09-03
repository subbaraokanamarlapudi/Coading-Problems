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