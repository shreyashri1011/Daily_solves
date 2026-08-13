from collections import deque

class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """

        if not root:
            return False

        queue = deque([(root, root.val)])

        while queue:

            curr, val = queue.popleft()

            # Check if current node is a leaf
            if not curr.left and not curr.right:

                if val == targetSum:
                    return True

            # Add left child
            if curr.left:
                queue.append((curr.left, val + curr.left.val))

            # Add right child
            if curr.right:
                queue.append((curr.right, val + curr.right.val))

        return False