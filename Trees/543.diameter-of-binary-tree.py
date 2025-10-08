#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter=0

        def count(root):
            if not root:
                return 0

            length_l=count(root.left)
            length_r=count(root.right)
            self.diameter=max(self.diameter, length_l+length_r)

            return 1+max(length_l,length_r)

        count(root)

        return self.diameter

        
# @lc code=end

