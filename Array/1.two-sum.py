#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        j=0
        temp=[]
        while i< len(nums):
            j=i+1
            while j< len(nums):
                if nums[j]+nums[i]==target:
                    temp.append(i)
                    temp.append(j)
                    return temp
                else:
                    j+=1
            i+=1
# @lc code=end

