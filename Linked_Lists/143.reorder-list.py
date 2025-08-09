#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next= None
        prev= None

        while second != None:
            temp = second.next
            second.next = prev
            prev = second
            second=temp

        second = prev
        first= head

        while second:
            temp1=first.next
            temp2=second.next
            first.next= second
            second.next = temp1
            first= temp1
            second= temp2

        
# @lc code=end

