## This is the most simplest assignment where in you are asked to solve
## the folowing problems, you may use the internet

'''
Problem - 0
Print the odd values in the given array
'''

arr = [5,99,36,54,88]

for i in arr:    
    if i % 2 != 0:
        print(i," ")
## Code Here

'''
Problem - 1
Print all the prime numbers from 0-100
'''
## Code Here
j = 2
while j < 100:
    k = 2
    while k < j:
        z = j - k
        if j % k == 0:
            break
        if z == 1:
            print(j)
        k=k+1
    j = j + 1
'''
Problem - 2
Print the reverse of a string
'''
string = 'Reverse Me!'
## Code Here
rev = ''
for i in string:
    rev=i+rev
print(rev)
