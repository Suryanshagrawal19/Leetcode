#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        res=[0]*n
        stack=[]
        for i, t in enumerate(temperatures):
            while stack and t> stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd]=(i-stackInd)
            stack.append([t,i])
        return res
# @lc code=end

