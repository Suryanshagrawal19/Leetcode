#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        temp=0

        l=0

        for r in range(len(s)):
            count[s[r]]=1+count.get(s[r],0)

            if (r-l+1)-max(count.values())>k:
                count[s[l]] -=1
                l+=1


            temp=max(temp,r-l+1)

        return temp
# @lc code=end

