#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        temp1= []
        temp2= []
        for i in s:
            temp1.append(i)
        for i in t: 
            temp2.append(i)
        return sorted(temp1) == sorted(temp2)
# @lc code=end

