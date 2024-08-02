"""
80. Remove Duplicates from Sorted Array II
Medium
Topics
Companies
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

"""
from typing import List

def removeDuplicates(nums: List[int]) -> int:
    counter = 0
    k = 0
    previous = 100000
    for i in range(len(nums)):
        if previous == nums[i]:
            counter += 1
        else:
            counter = 0
        previous = nums[i]
        if counter < 2:
            previous = nums[i]
            nums[k] = nums[i]
            k += 1
    return k

nums = [0,0,1,1,1,1,2,3,3]
print(removeDuplicates(nums))
print(nums)