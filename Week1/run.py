## This is the most simplest assignment where in you are asked to solve
## the folowing problems, you may use the internet
import math
'''
Problem - 0
Print the odd values in the given array
'''
arr = [5,99,36,54,88]
## Code Here

for number in arr:
    if number%2!=0:
        print(number)


'''
Problem - 1
Print all the prime numbers from 0-100
'''
## Code Here

for n in range(101):
    if n>1:
        is_prime = True
        for x in range(2,int(math.sqrt(n))+1):
            if n%x==0 :
                is_prime=False

        if is_prime:
            print(n)




'''
Problem - 2
Print the reverse of a string
'''

## Code Here
string = 'Reverse Me!'
reverse_string=string[::-1]
print(reverse_string)
