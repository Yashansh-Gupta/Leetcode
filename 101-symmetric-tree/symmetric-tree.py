# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """


        if root is None:
            return True

        return self.mirror(root.left, root.right)

    def mirror(self,p,q):
        if not p and q:
            return False
        if p and not q:
            return False
        if not p and not q:
            return True

        if p.val!=q.val:
            return False
        left=self.mirror(p.left, q.right)
        right=self.mirror( p.right,q.left)

        return left and right

