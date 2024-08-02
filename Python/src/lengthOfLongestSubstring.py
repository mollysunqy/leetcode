"""
3. Longest Substring Without Repeating Characters
Medium
Topics
Companies
Hint
Given a string s, find the length of the longest 
substring
 without repeating characters.

"""
def lengthOfLongestSubstring(s: str) -> int:
    max_length = 0
    i = 0
    substring = []
    for j in range(len(s)):
        if s[j] not in substring:
            max_length = max(max_length, j-i+1)
        else:
            while s[j] in substring:
                substring.pop(0)
                i += 1
        substring.append(s[j])

    return max_length
        

string = "abcabcbb"
print(lengthOfLongestSubstring(string))
