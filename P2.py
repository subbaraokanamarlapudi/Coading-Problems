'''
THIS QUESTION IS ASKED IN THE PREVIOUS YEAR TCS NQT

Joseph is learning digital logic subject which will be for his next semester. He usually tries to solve 
unit assignment problems before the lecture. Today he got one tricky question. The problem 
statement is “A positive integer has been given as an input. Convert decimal value to binary 
representation. Toggle all bits of it after the most significant bit including the most significant bit. 
Print the positive integer value after toggling all bits”. 

Constrains- 
1<=N<=100 

Example 1: 
Input : 
10  -> Integer 
Output : 
5    -> result- Integer 

Explanation: 
Binary representation of 10 is 1010. After toggling the bits(1010), will get 0101 which represents 
“5”. Hence output will print “5”. 
'''

decimal_value = int(input("Enter the decimal value: "))
binary_value = bin(decimal_value)[2:]

tv = ""

for i in range(len(binary_value)):
    if binary_value[i] == '1':
        tv += '0'
    else:
        tv += '1'

print(int(tv, 2))