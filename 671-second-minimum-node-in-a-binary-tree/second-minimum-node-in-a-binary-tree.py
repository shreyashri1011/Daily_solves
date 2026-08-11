from collections import deque

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        queue = deque([root])

        min_node = None
        second_min = None

        while queue:

            curr_node = queue.popleft()

            # Add children
            if curr_node.left:
                queue.append(curr_node.left)

            if curr_node.right:
                queue.append(curr_node.right)

            value = curr_node.val

            # First value we've seen
            if min_node is None:
                min_node = value

            # Found a new minimum
            elif value < min_node:
                second_min = min_node
                min_node = value

            # Found a value bigger than minimum
            elif value > min_node:
                if second_min is None or value < second_min:
                    second_min = value

        if second_min is None:
            return -1

        return second_min