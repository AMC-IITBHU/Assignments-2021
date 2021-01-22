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
    
    return string==string[::-1]

def sqrt_of_numbers(num):
    '''
    This function returns the magnitude of the square root of the number
    args:
        num (int) Need not be positive
    returns:
        sqroot (float)
    '''

    return math.sqrt(abs(num))

def Maximum(arr):
    '''
    This function returns first maximum and the second maximum
    number in the array
    args:
        arr (list)
    returns:
        Max1, Max2 (int, int)
    '''

    arr.sort(reverse=True)
    return arr[0], arr[1]

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

    arr.sort()
    e=[]
    b=[]
    for i in range(len(arr)):
        if arr[i]%2==0:
            e=np.append(e,arr[i])
        else:
            b=np.append(b,arr[i])
    
    return list(np.concatenate((e,b)))


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
    d= A[0]*B[1]-A[1]*B[0]
    if d!=0:
        x=(B[1]*C[0]-B[0]*C[1])/d
        y=(A[1]*C[0]-A[0]*C[1])/-d
        return  x,y
    else:
        return "x and y can be anything"
