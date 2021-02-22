## This is the most simplest assignment where in you are asked to solve
## the folowing problems, you may use the internet

'''
Problem - 0
Print the odd values in the given array
'''
arr = [5,99,36,54,88]
## Code Here
for i in arr:
	if i%2==1:
		print(i)

'''
Problem - 1
Print all the prime numbers from 0-100
'''
## Code Here
for i in range(1,101):
    if i<6 and i!=4:
        print(i)
    if i>6:
    	if (i%6==1 or i%6==5) and i%5!=0 and i!=49 and i!=77:
    		print(i)
'''
Problem - 2
Print the reverse of a string
'''
string = 'Reverse Me!'
## Code Here
x=[]
for i in range(len(string)):
	x.append(string[len(string)-i-1])
print(x)
