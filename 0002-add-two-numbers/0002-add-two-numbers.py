# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        new = ListNode()
        ans = new
        digit = False

        while l1 or l2 or digit:
            total = 0
            if digit:
                total += 1
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next

            digit = False if total < 10 else True
            new.next = ListNode(total % 10)
            new = new.next

        return ans.next
            
            