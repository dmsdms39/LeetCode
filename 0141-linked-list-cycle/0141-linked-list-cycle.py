# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p = head
        twice_p = head
        while twice_p and twice_p.next and twice_p.next.next:
            p = p.next
            twice_p = twice_p.next.next.next
            if p == twice_p:
                return True
        return False