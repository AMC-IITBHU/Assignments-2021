# assignment1
import math
import numpy as np

def demo(x):
    return x*x

def is_palindrome(string):
    temp = " "
    for i in string:
        temp = i + temp
    if temp == string:
        return True
    return False

def sqrt_of_numbers(num):
    if num >= 0:
        return math.sqrt(num)
    r = str(math.sqrt((abs(num))))+' i'
    return r

def Maximum(arr):
    arr.sort(reverse=True)
    return [arr[0], arr[1]]

def even_sort(arr):
    even = []
    odd = []
    for i in arr:
        if (i % 2 == 0):
            even.append(i)
        else:
            odd.append(i)
    even.sort()
    odd.sort()
    even.extend(odd)
    return even

def eqn_solver(A, B, C):
    m=A[0]
    n=B[0]
    if m > n:
        smaller = n
    else:
        smaller = m
    for i in range(1, smaller + 1):
        if ((m % i == 0) and (n % i == 0)):
            hcf = i
    prd = m * n
    lcm = prd / hcf
    m1 = lcm / A[0]
    m2 = lcm / B[0]
    y1 = A[1] * m1
    y2 = B[1] * m2
    y = y1 - y2
    c1 = C[0] * m1
    c2 = C[1] * m2
    cn = c1 - c2
    ya = cn / y
    xa = (C[0] - (A[1] * ya)) / A[0]
    print(xa)
    print(ya)
    return [xa,ya]
