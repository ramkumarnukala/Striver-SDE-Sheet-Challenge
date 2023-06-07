from os import *
from sys import *
from collections import *
from math import *

def merge(arr, temp, left, mid, right):
    count = 0
    i = left
    j = mid
    k = left

    while i <= mid -1 and j <= right:
        if arr[i] <= arr[j]:
            temp[k]=arr[i]
            i += 1
            k += 1
        else:
            temp[k]=arr[j]
            k += 1
            j += 1
            count += mid - i
    
    while i <= mid - 1:
        temp[k]=arr[i]
        i += 1
        k += 1

    while j <= right:
        temp[k] = arr[j]
        k += 1
        j += 1

    for i in range(left, right + 1):
        arr[i] = temp[i]
    
    return count
    
def getInversions(arr, temp, left, right) :
    out = 0
    if right > left:
        mid = (left + right)//2
        out += getInversions(arr, temp, left, mid)
        out += getInversions(arr, temp, mid + 1, right)
        out += merge(arr, temp, left, mid + 1, right)

    return out

# Taking inpit using fast I/O.
def takeInput() :
    n = int(input())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n

# Main.
arr, n = takeInput()
temp = [0] * n
print(getInversions(arr, temp, 0, n -1))