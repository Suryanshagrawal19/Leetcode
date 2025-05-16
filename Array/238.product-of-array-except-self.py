#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        temp= [1]*len(nums)
    

        mul1=1
        for i in range(len(nums)):
            temp[i] = mul1
            mul1 *=nums[i]
        
        mul2=1
        for i in range(len(nums)-1,-1,-1):
            temp[i]*=mul2
            mul2*=nums[i]

        return temp











        
    
                    
        
# @lc code=end

