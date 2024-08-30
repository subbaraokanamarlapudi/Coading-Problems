'''
4.Description:
write a progrm to perform given tasks Declare & initialize a number.Check whether the number is in range 0-100 or not.

If not in range print INVALID INPUT Else - if the number is in range 
91-100 then print SUPER SMART,
81-90 print SMART,
71-80 print SMART ENOUGH,
61-70 print JUST SMART,
36-60 print NO SMART,
0-35 print DUMB.

Constraints:
Input :          First line of input contains an Integer n reperesent number

Output :       Print their status

Example:
Input :       62

Output :   JUST SMART

Explanation:
here the input is in 61-70 range so you have to print JUST SMART

'''

# 1st Way

x = int(input("Enter a number: "))

if x >= 91 and x <= 100:
    print("SUPER SMART")
elif x >= 81 and x <= 90:
    print("SMART")
elif x >= 71 and x <= 80:
    print("SMART ENOUGH")
elif x >= 61 and x <= 70:
    print("JUST SMART")
elif x >= 36 and x <= 60:
    print("NO SMART")
elif x >= 0 and x <= 35:
    print("DUMB")
else:
    print("INVALID INPUT")


# 2nd way by using normal function.

def check_number(x):
    if x >= 91 and x <= 100:
        return "SUPER SMART"
    elif x >= 81 and x <= 90:
        return "SMART"
    elif x >= 71 and x <= 80:
        return "SMART ENOUGH"
    elif x >= 61 and x <= 70:
        return "JUST SMART"
    elif x >= 36 and x <= 60:
        return "NO SMART"
    elif x >= 0 and x <= 35:
        return "DUMB"
    else:
        return "INVALID INPUT"
    
result = check_number(62)
print(result)

# 3rd way by using lambda function.

x = eval(input("Enter a number: "))
check_number = lambda x: "SUPER SMART" if x >= 91 and x <= 100 else "SMART" if x >= 81 and x <= 90 else "SMART ENOUGH" if x >= 71 and x <= 80 else "JUST SMART" if x >= 61 and x <= 70 else "NO SMART" if x >= 36 and x <= 60 else "DUMB" if x >= 0 and x <= 35 else "INVALID INPUT"
result = check_number(x)
print(result)

# 4th way by using normal function using the user defined functions.

def check_number():
    x = eval(input("Enter a number: "))

    if x >= 91 and x <= 100:
        return "SUPER SMART"
    elif x >= 81 and x <= 90:
        return "SMART"
    elif x >= 71 and x <= 80:
        return "SMART ENOUGH"
    elif x >= 61 and x <= 70:
        return "JUST SMART"
    elif x >= 36 and x <= 60:
        return "NO SMART"
    elif x >= 0 and x <= 35:
        return "DUMB"
    else:
        return "INVALID INPUT"
    
result = check_number()
print(result)