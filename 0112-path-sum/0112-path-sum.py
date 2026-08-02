# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        def pathSum(Node, s):
            if Node is None:
                return False

            s += Node.val

            if Node.left is None and Node.right is None:
                return s == targetSum

            return pathSum(Node.left, s) or pathSum(Node.right, s)

        return pathSum(root, 0)
            
        