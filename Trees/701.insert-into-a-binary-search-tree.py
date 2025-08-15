#
# @lc app=leetcode id=701 lang=python3
#
# [701] Insert into a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        temp = root

        if not temp:
            return TreeNode(val)


        if val>temp.val:
                temp.right = self.insertIntoBST(temp.right, val)
        else:
                temp.left = self.insertIntoBST(temp.left, val)
        return temp
# @lc code=end

