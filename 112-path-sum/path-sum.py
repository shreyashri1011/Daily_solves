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
        if not root:
            return False
        stack=[(root,root.val)]
        while stack:
            curr,val=stack.pop()
            if not curr.left and not curr.right and val==targetSum:
                return True
            if curr.right:
                stack.append((curr.right,val+curr.right.val))
            if curr.left:
                stack.append((curr.left,val+curr.left.val))
        return False