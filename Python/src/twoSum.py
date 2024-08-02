"""
167. Two Sum II - Input Array Is Sorted
Medium

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.
"""
from typing import List


def twoSum(numbers: List[int], target: int) -> List[int]:
    result = []
    i = 0
    j = len(numbers)-1
    while(i<len(numbers) and j>=0 and i<j):
        sum = numbers[i] + numbers[j]
        if(sum == target):
            result = [numbers[i], numbers[j]]
            return result
        elif sum>target:
            j -= 1
        else:
            i += 1
    return result
        
numbers = [5,25,75]
r=twoSum(numbers,100)
print(r)