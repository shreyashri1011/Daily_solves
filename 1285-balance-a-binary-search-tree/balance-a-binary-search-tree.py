from collections import deque

class Solution(object):

    def inorder_traversal(self, root):
        nodes = []
        stack = []
        current = root

        while current or stack:

            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            nodes.append(current.val)

            current = current.right

        return nodes

    def balanceBST(self, root):

        if not root:
            return None

        # Convert TreeNode → sorted list
        nums = self.inorder_traversal(root)

        # NOW nums is a list
        n = len(nums)

        mid = n // 2

        new_root = TreeNode(nums[mid])

        q = deque()

        q.append((new_root, 0, mid - 1))
        q.append((new_root, mid + 1, n - 1))

        while q:

            parent, left, right = q.popleft()

            if left <= right:

                mid = (left + right) // 2

                child = TreeNode(nums[mid])

                if nums[mid] < parent.val:
                    parent.left = child
                else:
                    parent.right = child

                q.append((child, left, mid - 1))
                q.append((child, mid + 1, right))

        return new_root