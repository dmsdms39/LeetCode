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
        result = {}

        curr = head
        while curr:
            result[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            result[curr].next = result.get(curr.next)
            result[curr].random = result.get(curr.random)
            curr = curr.next

        return result[head]