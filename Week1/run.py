## This is the most simplest assignment where in you are asked to solve
## the folowing problems, you may use the internet

'''
Problem - 0
Print the odd values in the given array
'''
arr = [5, 99, 36, 54, 88]
## Code Here
for  num in arr:
    if num % 2 !=0:
        print(num)
'''
Problem - 1
Print all the prime numbers from 0-100
'''
## Code Here
for num in range(0, 100):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)

'''
Problem - 2
Print the reverse of a string
'''
string = 'Reverse Me!'
## Code Here
print(string[::-1])
