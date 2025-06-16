# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        # count the number of nodes in the ListNode
        cnt = 1
        curr = head
        while curr.next:
            curr = curr.next
            cnt += 1

        # minimize the number of rotations
        k = k % cnt

        # if no rotation needed
        if k == 0:
            return head

        # find the new tail
        new_tail = head

        for _ in range(cnt - k - 1):
            new_tail = new_tail.next
        
        new_head = new_tail.next

        # find the previous node of the new head
        head_prev = new_head

        for _ in range(k - 1):
            head_prev = head_prev.next
        head_prev.next = head

        new_tail.next = None

        return new_head




