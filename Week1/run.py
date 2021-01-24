## This is the most simplest assignment where in you are asked to solve
## the folowing problems, you may use the internet

'''
Problem - 0
Print the odd values in the given array
'''
arr = [5,99,36,54,88]
## Code Here
i=0
count=0
while(i<5)
  if(arr[0]%2!=0)
    count+=1
  i+=1
 print(count)
'''
Problem - 1
Print all the prime numbers from 0-100
'''
i=1
while(i=<100)
  i+=1;
  w=2;
  if(i==2)
    print(2);
  else
    a=true
    while(w<i)
      if(i%w==0)
        a=false
        break
      w+=1        
    if(a)
      print(i)
## Code Here

'''
Problem - 2
Print the reverse of a string
'''
string = 'Reverse Me!'
## Code Here,
i=10
while(i>=0)
  print(string[i])
  i-=1
