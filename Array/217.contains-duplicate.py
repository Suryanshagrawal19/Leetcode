#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
       temp = set()
       if len(nums) == 0:
          return False
       for i in nums:
            if i not in temp:
                temp.add(i)
            else:
                return True
       return False
        
# @lc code=end
