# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        dq = deque()
        dq.append(root)
        array = []
        while dq:
            node = dq.popleft()
            array.append(node.val)

            if node.left: 
                dq.append(node.left)
            if node.right: 
                dq.append(node.right)

        array.sort()

        answer = float("inf")
        for i in range(1, len(array)):
            answer = min(answer, array[i] - array[i-1])
            if answer == 1: break

        return answer