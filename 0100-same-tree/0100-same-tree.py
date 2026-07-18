# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        arr1 = []
        arr2 = []
        
        def preorder(root, arr):
            if root is None:
                arr.append(None)
                return
            arr.append(root.val)
            preorder(root.left, arr)
            preorder(root.right, arr)
            
        preorder(p, arr1)
        preorder(q, arr2)
        return arr1==arr2