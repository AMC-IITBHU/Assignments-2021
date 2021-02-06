## This is the most simplest assignment where in you are asked to solve
## the folowing problems, you may use the internet

'''
Problem - 0
Print the odd values in the given array
'''
arr = [5,99,36,54,88]
## Code Here
for i in range(len(arr)):
    if(arr[i] & 1):
      print(arr[i],end=" ")

'''
Problem - 1
Print all the prime numbers from 0-100
'''
## Code Here
sieve=[i for i in range(0,101)]
for i in range(2,11):
  if(sieve[i]):
    for j in range(i*i,len(sieve),i):
      sieve[j]=0
for i in range(2,len(sieve)):
  if(sieve[i]):
    print(sieve[i],end=" ")

'''
Problem - 2
Print the reverse of a string
'''
string = 'Reverse Me!'
## Code Here
for i in range(-1,-len(string),-1):
  print(string[i])
