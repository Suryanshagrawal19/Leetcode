class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i=0
        j=1
        while i<len(nums) and j<len(nums):
            j=i+1
            while j<len(nums):
                if nums[i]==nums[j]:
                    nums.remove(nums[j])
                else:
                    j+=1
            i+=1
        return len(nums)
