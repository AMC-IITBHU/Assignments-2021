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
    m=string.lower()
    s=''
    for i in m:
        s=i+s
    if s==m:
        c=True
    else:
        c=False
    
    return c
    

def sqrt_of_numbers(num):
    '''
    This function returns the magnitude of the square root of the number
    args:
        num (int) Need not be positive
    returns:
        sqroot (float)
    '''

    new_num=abs(num)
    
    return math.sqrt(new_num)


def Maximum(arr):
    '''
    This function returns first maximum and the second maximum
    number in the array
    args:
        arr (list)
    returns:
        Max1, Max2 (int, int)
    '''

    lst=sorted(arr)
    Max1=lst[-1]
    Max2=lst[-2]
    return Max1,Max2

    

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

    even_list=[]
    odd_list=[]

    for i in arr:
        if i%2==0:
            even_list.append(i)
        else:
            odd_list.append(i)
    odd_list.sort()
    even_list.sort()
    n_list=even_list+odd_list        
            
            
    return n_list
   


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

    x=np.array([A,B])
    y=np.array(C)
    soln=np.linalg.solve(x,y)
    x=soln[0]
    y=soln[1]
    

    return x,y

   
