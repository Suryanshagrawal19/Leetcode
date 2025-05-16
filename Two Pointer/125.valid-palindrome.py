#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        joined= "".join(s.split())
        temp=[]
        for i in joined:
            if i.isalpha() or i.isdigit():
                temp.append(i.lower())
        
        j=0
        k=len(temp)-1

        while j<len(temp):
            if temp[j]==temp[k]:
                j+=1
                k-=1
            else:
                return False
    
        return True

            
        
        
# @lc code=end

