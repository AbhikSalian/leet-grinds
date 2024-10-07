# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head:
            return 0
        maxsum=0
        slow,fast=head,head
        prev=None
        while fast and fast.next:
            fast=fast.next.next
            temp=slow.next
            slow.next=prev
            prev=slow
            slow=temp
        left,right=slow,prev
        while left:
            maxsum=max(maxsum,left.val+right.val)
            left=left.next
            right=right.next
        return maxsum