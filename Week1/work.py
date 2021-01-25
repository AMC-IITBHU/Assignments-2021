import math
import numpy as np

def demo(x):
    return x*x

def is_palindrome(string):
    t = int(len(s)/2)
    for i in range(0, t):
        if s[i] != s[len(s)-i-1]:
            return 0
    else:
        return 1
   

def sqrt_of_numbers(num):
    return sqrt(num)
def Maximum(arr):
   Max = max(arr)
   arr.remove(min(arr))
   sec_min = min(arr)
    
   return Max, sec_min


def even_sort(arr):
    even = []
    arr1 = []
    for i in arr:
        if i % 2 == 0:
            even.append(i)
        else:
            arr1.append(i)
    for i in range(0, len(even)):
        for j in range(i + 1, len(even)):
            if even[i] > even[j]:
                even[i], even[j] = even[j], even[i]
    for i in range(0, len(arr1)):
        for j in range(i + 1, len(arr1)):
            if arr1[i] > arr1[j]:
                arr1[i], arr1[j] = arr1[j], arr1[i]
    arr = even + arr1
    return arr



def eqn_solver(A, B, C):
    x = (C[0]*A[1]-C[1]*A[0])/(A[1]*B[0]-A[0]*B[1])
    y = (C[0]*B[1]-C[1]*B[0])/(B[1]*A[0]-B[0]*A[1])
    
    return x,y
