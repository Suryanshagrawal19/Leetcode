#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = ListNode(0, head)
        i= temp
        for a in range(n+1):
            i=i.next
        j= temp
        while i:
            i=i.next
            j=j.next

        j.next=j.next.next   

        return temp.next
# @lc code=end

