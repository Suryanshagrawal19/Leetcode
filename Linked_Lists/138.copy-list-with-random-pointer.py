#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head==None:
            return None


        old={}

        curr=head

        while curr:
            copy=Node(curr.val)
            old[curr]=copy
            curr=curr.next

        curr=head
        while curr:
            copy= old[curr]
            if curr.next == None:
                copy.next = None
            else:
                copy.next=old[curr.next] 
            if curr.random == None:
                copy.random= None
            else: 
                copy.random=old[curr.random]
            curr=curr.next
        return old[head]
# @lc code=end

