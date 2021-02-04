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
    reversed_string = string[::-1]
    
    if reversed_string == string:
        return bool(1)
    else:
        return bool(0)
    
    

def sqrt_of_numbers(num):
    '''
    This function returns the magnitude of the square root of the number
    args:
        num (int) Need not be positive
    returns:
        sqroot (float)
    '''

    ## Code Here
    return np.sqrt(abs(num))

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
    x1 = np.sort(arr)[-1]
    x2 = np.sort(arr)[-2]
    return x1,x2

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
    even = []
    odd = []

    for i in arr:
        if i %2 == 0:
            even.append(i)
        else:
            odd.append(i)

    even = np.sort(even)
    odd = np.sort(odd)

    arr =[]
    for i in even:
        arr.append(i)
    for i in odd:
        arr.append(i)
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
    x1, x2 = A
    y1, y2 = B
    c1, c2 = C

    coeff_matrix = np.array([[x1, y1], [x2, y2]])
    const_matrix = np.array([[c1], [c2]])
    inverse = np.linalg.inv(coeff_matrix)
    actual = np.dot(inverse,const_matrix)
    d = actual.reshape(1,-1)
    x = d[0][0]
    y = d[0][1]
  
    return x,y
    
    
