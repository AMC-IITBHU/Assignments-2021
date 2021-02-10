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
    
    return x**2
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
    
    string1=string.lower()
    if string1==string1[::-1]:
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
    
    if num>0:
        num=num
    else:
        num=-num
    x=sqrt(num)
    return x
    
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
    
    arr.sort()
    n=len(arr)
    max1=arr[n-1]
    max2=arr[n-2]
    return max1,max2

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
    
    arr=array([15,2,6,88,7])
    even_arr=([])
    odd_arr=([])
    for i in arr:
        if i%2==0:
            even_arr.append(i)
        else:
            odd_arr.append(i)
        
    even_arr.sort()
    odd_arr.sort()
    
    ans=concatenate((even_arr,odd_arr))
    return ans

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
    
    x = np.array([A, B])
    y = np.array(C)
    sol = np.linalg.solve(x, y)
    x=sol[0]
    y=sol[1]
    return x,y

