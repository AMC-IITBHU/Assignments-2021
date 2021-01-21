## This is the most simplest assignment where in you are asked to solve
## the folowing problems, you may use the internet

'''
Problem - 0
Print the odd values in the given array
'''
arr = [5,99,36,54,88]
for k in arr:
  if k%2==1:
    print(k)
  
'''
Problem - 1
Print all the prime numbers from 0-100
'''
for j in range(2,101):
    for m in range(2,j):
        if j%m==0:
            break
    else:
        print(j)

'''
Problem - 2
Print the reverse of a string
'''
string = 'Reverse Me!'
s=''
a='pyhton lovers'
for i in a:
    s=i+s
print(s)
