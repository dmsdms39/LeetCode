# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pStack = [p]
        qStack = [q]

        while pStack and qStack:
            pNode = pStack.pop()
            qNode = qStack.pop()

            if pNode and qNode:
                if pNode.val != qNode.val:
                    return False
                else:
                    pStack.extend([pNode.left,pNode.right])
                    qStack.extend([qNode.left,qNode.right])
                    
            elif not pNode and not qNode:
                continue

            else:
                return False

        return len(pStack) == len(qStack) 
    