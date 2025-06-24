#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=1
        temp=0
        while r <len(prices):
            if prices[r]<prices[l]:
                l=r
            else:
                profit= prices[r]-prices[l]
                temp= max(temp, profit)
            r+=1
        return temp
# @lc code=end

