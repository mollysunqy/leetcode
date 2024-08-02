"""
71. Simplify Path
Medium
Topics
Companies
Given an absolute path for a Unix-style file system, which begins with a slash '/', transform this path into its simplified canonical path.

In Unix-style file system context, a single period '.' signifies the current directory, a double period ".." denotes moving up one directory level, and multiple slashes such as "//" are interpreted as a single slash. In this problem, treat sequences of periods not covered by the previous rules (like "...") as valid names for files or directories.

The simplified canonical path should adhere to the following rules:

It must start with a single slash '/'.
Directories within the path should be separated by only one slash '/'.
It should not end with a slash '/', unless it's the root directory.
It should exclude any single or double periods used to denote current or parent directories.
Return the new path.
"""

def simplifyPath(path: str) -> str:
    folders = path.split('/')
    shortest = []
    for f in folders:
        if f == "..":
            if shortest:
                shortest.pop()
        elif f == "." or f == "":
            continue
        else:
            shortest.append(f)
    shortest_string = ""
    for s in shortest:
        shortest_string = shortest_string +"/" + s
    if shortest_string == "":
        return "/"
    return shortest_string

file_name = "/../"


print(simplifyPath(file_name))