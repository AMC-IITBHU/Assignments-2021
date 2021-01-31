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
    return (x*x)

def is_palindrome(string):
    '''
    This function returns True if the given string is
    a Palindrome
    args:
        string (str)
    returns:
        flag (bool)
    '''

    ## Code Here
    l=len(string)
    pal=''
    for i in range(0,l):
        pal+=string[l-1-i]
    if pal==string:
        return True
    else:
        return False

def sqrt_of_numbers(num):
    '''
    This function returns the magnitude of the square root of the number
    args:
        num (int) Need not be positive
    returns:
        sqroot (float)
    '''

    ## Code Here
    if num<0:
        num=-num
    sq=math.sqrt(num)    
    return sq

def Maximum(arr):
    '''
    This function returns first maximum and the second maximum
    number in the array
    args:
        arr (list)
    returns:
        Max1, Max2 (int, int)
    '''

    ## Code Here
    l=len(arr)
    for i in range(0,l):
        for j in range(0,l-i-1):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    return arr[l-1],arr[1]

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

    ## Code Here
    l=len(arr)
    c=0
    for i in range(0,l):
        if arr[i]%2==0:
            for j in range(0,i):
                if arr[j]%2==1:
                    temp=arr[j]
                    arr[j]=arr[i]
                    arr[i]=temp
    for i in range(0,l):
        if arr[i]%2==0:
            c+=1
    for i in range(0,c):
        for j in range(0,c-i-1):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
    for i in range(c,l):
        for j in range(c,l-i-1+c):
            if arr[j]>arr[j+1]:
                tem=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=tem
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

    ## Code Here
    d=(A[0]*B[1])-(A[1]*B[0])
    if d==0:
        return False
    x=((C[0]*B[1])-(C[1]*B[0]))/d
    y=((C[1]*A[0])-(C[0]*A[1]))/d
    return x,y
