# 20. Valid Parentheses (Grind75 #2)
# 2024-04-17

# Approach
# First attempt was to simply loop through and check if any opened brackets closed - 71/98
# Second attempt was to split list in half, reverse the second half and the two halves - failed on [](){}
# Third attempt was to loop and check if the next element was a different type of closing bracket - 84/98
# Fourth attempt: Used hint from leetcode to use stack and tracked opening/closing brackets - Accepted

# Complexity
# Time: O(n)

"""
# Notes:
if len(s)%2 !=0:
    return False
# I thought this would reduce time, and make the program faster, but it didn't.
# Removing this line saved 5 ms on Leetcode
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == "{" or i == "(" or i == "[":
                stack.append(i)
            else:
                # Only remove matching bracket if it was at the top of the stack
                if len(stack) >0:
                    top = stack[-1]
                    if i == "}" and top == "{":
                        stack.pop()
                    elif i == ")" and top == "(":
                        stack.pop()
                    elif i == "]" and top == "[":
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        # There should be no opening brackets left in the stack
        if len(stack) == 0:
            return True
        return False