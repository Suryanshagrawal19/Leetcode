#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1

        while l<=r:
            m=(l+r)//2
            if nums[m]==target:
                return m
            if nums[l]<=nums[m]:
                if nums[l]<=target<nums[m]:
                   r=m-1
                else:
                    l=m+1
            else:
                if nums[m]<target<=nums[r]:
                    l=m+1
                else:
                    r=m-1
        return -1


        # @lc code=end

