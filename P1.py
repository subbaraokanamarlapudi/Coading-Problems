'''
THIS QUESTION IS  ASKED IN THE PREVIOUS YEAR TCS NQT

QUESTION 1
A chocolate factory is packing chocolates into the packets. The chocolate packets here represent 
an array  of N number of integer values. The task is to find the empty packets(0) of chocolate and 
push it to the end of the conveyor belt(array).

Example 1 : 
N=8 and arr = [4,5,0,1,9,0,5,0]
Output: 
4 5 1 9 5 0 0 0 

'''

n = 8
arr = [4,5,0,1,0,9,0,5,0]

for i in range(n):
    if arr[i] == 0:
        arr.remove(arr[i])
        arr.append(0)
print(arr)

