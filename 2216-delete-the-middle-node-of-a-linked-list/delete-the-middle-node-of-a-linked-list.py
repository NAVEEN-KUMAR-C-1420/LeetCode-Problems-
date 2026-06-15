# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=fast=head
        prev=head
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        if prev.next:
            prev.next=slow.next
        else:
            head=None
        print(prev.val)
        return head