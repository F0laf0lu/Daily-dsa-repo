# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        val_set = set()
        curr = head
        prev = None
        while curr:
            if curr.val in val_set:
                prev.next = curr.next
            else:
                val_set.add(curr.val)
                prev = curr
            curr = curr.next
        return head
            
