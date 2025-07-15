# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        p, slow, fast = None, head, head

        while fast and fast.next:
            p = slow
            slow = slow.next
            fast = fast.next.next
        p.next = None
        # p group과 slow/fast group

        return self.merge(self.sortList(head), self.sortList(slow))

    def merge(self, l1, l2):
        dummyNode = ListNode(None)
        current = dummyNode

        while l1 and l2:
            if l1.val > l2.val :
                current.next, l2 = l2, l2.next
            else :
                current.next, l1 = l1, l1.next
            current = current.next

        # 비교 후 남은 숫자들 붙이기
        if l1 :
            current.next = l1
        elif l2 :
            current.next = l2

        return dummyNode.next
