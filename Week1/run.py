## This is the most simplest assignment where in you are asked to solve
## the folowing problems, you may use the internet

'''
Problem - 0
Print the odd values in the given array
'''
arr = [5, 99, 36, 54, 88]
## Code Here
print("odd values are:-")
for i in range(0, 4):
    if arr[i] % 2 == 1:
        print(arr[i])

'''
Problem - 1
Print all the prime numbers from 0-100
'''
## Code Here
for i in range(2, 100):
    for j in range(2, i):
        if (i % j == 0):
            break
    else:
        print(i)

'''
Problem - 2
Print the reverse of a string
'''
string = 'Reverse Me!'
## Code Here
print(string[::-1])
