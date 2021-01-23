## This is the most simplest assignment where in you are asked to solve
## the folowing problems, you may use the internet

'''
Problem - 0
Print the odd values in the given array
'''
arr = [5,99,36,54,88]
## Code Here
for i in arr:
    if i%2==0:
        pass
    else:
        print(i)

'''
Problem - 1
Print all the prime numbers from 0-100
'''
## Code Here
for i in range(0,101):
    for a in range(2,i):
        if i%a==0:
            break
    else:
        print(i)
'''
Problem - 2
Print the reverse of a string
'''
string = 'Reverse Me!'
## Code Here
string='Reverse Me!'[::-1]
print(string)
