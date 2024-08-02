"""

6. Zigzag Conversion
Medium
Topics
Companies
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 
 """
import math


def convert(s: str, numRows: int) -> str:
    str_list = []
    for _ in range(numRows):
        str_list.append("")
    i = 0
    k = 0
    order = True
    while(i<len(s)):

        str_list[k] = str_list[k] + s[i]
        i += 1
        if k == numRows-1 and order:
            order = False
        elif k <= 0 and not order:
            order = True
        if order:
            k += 1
        else:
            k -= 1
    result = ""
    for z in str_list:
        result = result + z
    return result

s = "ABC"
print(convert(s,1))