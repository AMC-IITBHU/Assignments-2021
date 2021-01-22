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

    ## Code Here
    mod_string = ""
    for i in range(len(string)):
        mod_string += string[len(string)-i-1]
    
    if(mod_string.lower() == string.lower()):
      flag = True
    else:
      flag = False
     
    return flag

def sqrt_of_numbers(num):
    '''
    This function returns the magnitude of the square root of the number
    args:
        num (int) Need not be positive
    returns:
        sqroot (float)
    '''

    ## Code Here
    if(num<0):
        num = -num
    return math.sqrt(num)

def Maximum(arr):
    '''
    This function returns first maximum and the second minimum
    number in the array
    args:
        arr (list)
    returns:
        Max1, Max2 (int, int)
    '''

    ## Code Here
    a = np.max(arr)
    b = np.min(arr)
    indices = np.where(arr == b)

    for i in indices:
      arr = np.delete(arr, i)
    
    b = np.min(arr)
    return a, b

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
    a = []
    b = []
    for i in arr:
      j = 0
      k = 0
      if i%2==0:
        a = np.insert(a, j, i)
        j += 1
      else:
        b = np.insert(b, k, i)
        k += 1
    
    a = np.sort(a)
    b = np.sort(b)
    c = np.concatenate((a,b)) 
    return c


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
    x = (B[1]*C[0]-B[0]*C[1])/(B[1]*A[0]-B[0]*A[1])
    y = (C[0]-A[0]*x)/B[0]
    return x, y
