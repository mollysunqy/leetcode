
"""
15. 3Sum
Medium
Topics
Companies
Hint
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""
from typing import List

def threeSum( nums: List[int]) -> List[List[int]]:
    nums.sort()
    result = set()
    i=0
    while ( i < len(nums)-2):

        target = 0 - nums[i]
        j = i+1
        k = len(nums)-1
        while(j<len(nums) and k>=0 and j<k):
            sum = nums[k] + nums[j]
            if(sum == target):
                result.add( (nums[i], nums[j], nums[k]))
                j += 1
                k -= 1
            elif sum>target:
                k -= 1
            else:
                j += 1
        i += 1
    result_list = []
    for t in result:
        result_list.append(list(t))
    return result_list

nums = [-1,0,1,2,-1,-4]
r = threeSum(nums)
print(r)