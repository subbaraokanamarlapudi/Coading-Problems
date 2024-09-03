'''
6.Description:
write a program to convert kg values into gram values?

Constraints:
Input :           First line of input contains a decimal value represent weight in kgs

Output :        Print weight in grams

Example:
Input :          5.6

Output :       5600 Grams

Explanation:
in the above example we have to convert the 5.6kg to grams so you have to print 5600Grams.

'''

# 1st way
x = eval(input("Enter the weight in kgs: "))
y = int(x*1000)     # Type casting
print(y,"Grams")

# 2nd way

def kg_to_grams(kg):
    return int(kg * 1000)
kg = float(input("Enter the weight in kgs: "))
grams = kg_to_grams(kg)
print(grams, "Grams")

# 3rd way

def kg_to_grams():
    kg = float(input("Enter the weight in kgs: "))
    grams = int(kg * 1000)
    print(grams, "Grams")

kg_to_grams()

