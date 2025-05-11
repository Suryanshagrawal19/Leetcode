#
# @lc app=leetcode id=1929 lang=python3
#
# [1929] Concatenation of Array
#

# @lc code=start
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[]
        i=0
        while i< len(nums):
            ans.append(nums[i])
            i+=1
            if i==len(nums):
                i=0
                while i< len(nums):
                    ans.append(nums[i])
                    i+=1
                return ans

        
# @lc code=end

