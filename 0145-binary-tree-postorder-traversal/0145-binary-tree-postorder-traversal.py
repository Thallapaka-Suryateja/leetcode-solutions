# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        res=[]
        def postOrder(root,res):
            if root is None:
                return
            postOrder(root.left,res)
            postOrder(root.right,res)
            res.append(root.val)
        postOrder(root,res)
        return res
