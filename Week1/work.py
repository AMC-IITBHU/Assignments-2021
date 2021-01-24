import math
import numpy as np

def demo(x):
    '''
    This is a demo function
    Where in you just return square of the number
    args:
        x (int)
    returns:
        x*x (int)
    '''

    ## Code Here
    return x*x

def is_palindrome(string):
    '''
    This function returns True if the given string is
    a Palindrome
    args:
        string (str)
    returns:
        flag (bool)
    '''

   
    n=len(str)
    flag=0
    str=str.lower()
    for i in range(0,n/2):
        if(str[i]==str[n-1-i]):
            flag="True"
        else:
            flag="False"
    return flag

def sqrt_of_numbers(num):
    '''
    This function returns the magnitude of the square root of the number
    args:
        num (int) Need not be positive
    returns:
        sqroot (float)
    '''

  
    num=abs(num)
    num=num ** 0.5
    
   
    return float(num)

def Maximum(arr):
    '''
    This function returns first maximum and the second minimum
    number in the array
    args:
        arr (list)
    returns:
        Max1, Max2 (int, int)
    '''

  
    arr.sort()
    
   
    
  
    return arr[-1],arr[-2]

def even_sort(arr):
    '''
    This function sorts the array giving higher preference to even numbers
    args:
        arr (list)
    returns:
        sort_arr (list)
    ex:
        arr = [15, 2, 6, 88, 7]
        ## then
        sort_arr = [2, 6, 88 ,7 ,15]
        ## This is any even number is smaller than any odd number
    '''

   
    arr1=[]
    arr2=[] 
    sort_arr=[]

 
    arr.sort()
    for i in arr:
        
            
       
            if(arr[i]%2==0):
               arr1.append(arr[i])
            else:
                arr2.append(arr[i])
                
               
    
    sort_arr=arr1+arr2
   

   
    return sort_arr


def eqn_solver(A, B, C):
    '''
    This function solves a two variable system
    i.e.,
        A = [ 1, 2 ]
        B = [ 3, 4 ]
        C = [ 5, 6 ]
        then it means
        1x + 3y = 5
        2x + 4y = 6
        Hence you are required to find x, y for such a linear system
    args:
        A, B, C (list, list, list) representing coefficients in the equation
    returns:
        x, y (float, float)
    '''

      
    x=float((C[0]*B[1])-(C[1]*B[0]))/((B[1]*A[0])-(A[1]*B[0]))
    y=float((C[0]*A[1])-(C[1]*A[0]))/((B[0]*A[1])-(A[0]*B[1]))

   
    return float(x),float(y)
