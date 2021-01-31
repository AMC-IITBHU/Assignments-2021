import math
#import numpy as np

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
    return  x*x

def is_palindrome(string):
    '''
    This function returns True if the given string is
    a Palindrome
    args:
        string (str)
    returns:
        flag (bool)
    '''
    x=True
    a=len(string)
    i=0
    while(i<a):
        if(string[i]!=string[a-i-1]):
            x=False
        i+=1
    ## Code Here
    return x

def sqrt_of_numbers(num):
    '''
    This function returns the magnitude of the square root of the number
    args:
        num (int) Need not be positive
    returns:
        sqroot (float)
    '''
    if(num<0):
        num=-1*num
    ## Code Here
    return num**0.5

def Maximum(arr):
    '''
    This function returns first maximum and the second minimum
    number in the array
    args:
        arr (list)
    returns:
        Max1, Max2 (int, int)
    '''
    for i in range(0,len(arr),1):
        for j in range(i,len(arr),1):
            if(arr[i]>arr[j]):
                a=arr[i]
                arr[i]=arr[j]
                arr[j]=a
        
    ## Code Here
    return arr[0],arr[len(arr)-1]

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
    
    for i in range(0,len(arr),1):
        one=arr[i]
        for j in range(i,len(arr),1):
            if(arr[i]%2==0):
                if((arr[j]%2==0)and(arr[i]>arr[j])):
                    one=arr[i]
                    arr[i]=arr[j]
                    arr[j]=one
            else:
                if(arr[j]%2==0 or (arr[i]>arr[j])):
                    one=arr[i]
                    arr[i]=arr[j]
                    arr[j]=one
                    

    return arr


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
    y=(A[0]*C[1]-A[1]*C[0])/(A[0]*B[1]-A[1]*B[0])
    x=((B[0]*C[1]-B[1]*C[0])/(B[0]*A[1]-B[1]*A[0]))
    ## Code Here
    return (x,y)