"""
202. Happy Number
Easy
Topics
Companies
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
"""

def isHappy(n: int) -> bool:
    digits_map = set()
    sum = n
    while sum != 1:
        string = str(sum)
        if string in digits_map:
            return False
        sum = 0
        digits_map.add(string)
        for c in string:
            sum += int(c) ** 2
    return True

print(isHappy(2))
        