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
    

    ## Code Here
    

def is_palindrome(string):
    '''
    This function returns True if the given string is
    a Palindrome
    args:
        string (str)
    returns:
        flag (bool)
    '''
    rev=''.join(reversed(string))
    if (string==rev):
     return True
     return False

    ## Code Here
    

def sqrt_of_numbers(num):
    '''
    This function returns the magnitude of the square root of the number
    args:
        num (int) Need not be positive
    returns:
        sqroot (float)
    '''
    num=abs(num)
    x=math.sqrt(num)
    return float(x)
    ## Code Here
   

def Maximum(arr):
    '''
    This function returns first maximum and the second minimum
    number in the array
    args:
        arr (list)
    returns:
        Max1, Max2 (int, int)
    '''
    large=arr[0]
    slarge=-1
    for i in range(1,len(arr)):
         if (arr[i]>large):
            slarge=large
            large=arr[i]
         elif(slarge<arr[i]):
            slarge=arr[i] 
            
            
    return large,slarge 
    ## Code Here
    

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
    even=[]
    for num in arr:
        if num % 2 == 0:
            even.append(num)
    odd=[]
    for num in arr:
        if not num % 2 == 0:
            odd.append(num)
    even.sort()
    odd.sort()

    result = even + odd

    return result 
    ## Code Here
    


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
      a1, a2 = A
      b1, b2 = B
      c1, c2 = C

      coeff = np.array([[a1, b1], [a2, b2]])
      constant = np.array([[c1], [c2]])
      inv = np.linalg.inv(coeff)
      actual = np.dot(inv,constant)
      d = actual.reshape(1,-1)
      x = d[0][0]
      y = d[0][1]

      return x,y
    ## Code Here
   
