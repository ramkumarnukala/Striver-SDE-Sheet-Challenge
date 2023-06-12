from os import *
from sys import *
from collections import *
from math import *

def getLongestSubarray(nums: [int], k: int) -> int:
    n = len(nums)
    sum = 0
    maxi = 0
    map = {}
    for i in range(n):
        sum += nums[i]
        if sum == k:
            maxi = max(maxi, i+1)
        rem = sum - k
        if rem in map:
            maxi = max(maxi, i - map[rem])
        if sum not in map:
            map[rem] = i
    return maxi