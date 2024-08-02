"""
209. Minimum Size Subarray Sum
Medium
Topics
Companies
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

"""
from typing import List

def minSubArrayLen(target: int, nums: List[int]) -> int:
    i = 0
    sum = 0
    min_length = 1000000
    current_length =0
    for j in range(len(nums)):
        sum += nums[j]
        while sum >= target:
            min_length = min(min_length, j-i+1)
            i += 1
            sum -= nums[i]
    if min_length == 1000000:
        return 0
    else:
        return min_length
    
        

nums = [2,3,1,2,4,3]
r = minSubArrayLen(11,nums)
print(r)