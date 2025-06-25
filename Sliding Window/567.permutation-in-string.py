#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count={}
        for r in (s1):
            count[r] = 1 + count.get(r, 0)
            
        temp = len(s1)
        i=0
        j=0
        count2={}
        for j in range(len(s2)):
            count2[s2[j]] = 1 + count2.get(s2[j], 0)

            if (j-i+1)>temp:
                count2[s2[i]]-=1
                if count2[s2[i]] == 0:
                    del count2[s2[i]]
                i+=1

            if count2==count:
                return True
        return False
# @lc code=end

