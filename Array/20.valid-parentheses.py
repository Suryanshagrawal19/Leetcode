#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack= []
        closeToOpen= {")":"(","}":"{","]":"["}
        for i in s:
            if i in closeToOpen:
                if stack and stack[-1]==closeToOpen[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return len(stack)==0
        


            
            
            
           
                



        
# @lc code=end

