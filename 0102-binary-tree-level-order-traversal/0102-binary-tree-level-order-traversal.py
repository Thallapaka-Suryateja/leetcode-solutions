# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        arr=[]
        if root is None:
            return []
        def lorder(root,level):
            if root is None:
                return 
            if len(arr) <= level:
                arr.append([])
            arr[level].append(root.val)
            lorder(root.left,level+1)
            lorder(root.right,level+1)
    
        lorder(root,0)
        return arr