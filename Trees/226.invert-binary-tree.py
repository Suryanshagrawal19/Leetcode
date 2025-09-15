#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        temp=root
        if temp != None:
            temp.left,temp.right=temp.right,temp.left

            self.invertTree(temp.left)
            self.invertTree(temp.right)

        return temp
# @lc code=end

