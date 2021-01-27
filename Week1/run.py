## This is the most simplest assignment where in you are asked to solve
## the folowing problems, you may use the internet

'''
Problem - 0
Print the odd values in the given array
'''
arr = [5,99,36,54,88]
## Code Here
i=0
while i<5:
    if arr[i]%2!=0:
        print(arr[i])
    i+=1    

'''
Problem - 1
Print all the prime numbers from 0-100
'''
## Code Here
def is_prime(x):
    i=2
    while i<x:
        if x%i==0:
            return 0
            break
        i+=1
    if i==x:
        return 1
num=2
while num<=100:
    if is_prime(num):
        print(num)
    num+=1    
'''
Problem - 2
Print the reverse of a string
'''
string = 'Reverse Me!'
## Code Here
string=string[::-1]
print(string)  
