# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root is None:
            return True

        leftHeight = self.maxDepth(root.left)
        rightHeight = self.maxDepth(root.right)
        if abs(leftHeight - rightHeight) > 1:
            return False
        
        else:
            left=self.isBalanced(root.left)
            right=self.isBalanced(root.right)

            return left and right

    def maxDepth(self,root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        left=self.maxDepth(root.left)
        right=self.maxDepth(root.right)

        return max(left,right)+1