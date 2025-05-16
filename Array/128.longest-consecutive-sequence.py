#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       if nums==[]:
           return 0
      
       s= sorted(nums)
       max_count=1
       count=1


       for i in range(len(s)-1):
           if s[i]==s[i+1]:
               continue
           if s[i]+1==s[i+1]:
               count+=1
           else:
               max_count=max(max_count,count)
               count=1
       return max(max_count, count)
            
        
# @lc code=end

