# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):

    def deleteNode(self, root, key):

        # Tree is empty
        if root is None:
            return None

        # Key is smaller → go left
        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        # Key is larger → go right
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        # We found the node
        else:

            # Case 1: No children
            if root.left is None and root.right is None:
                return None

            # Case 2: Only right child
            elif root.left is None:
                return root.right

            # Case 3: Only left child
            elif root.right is None:
                return root.left

            # Case 4: Two children
            else:
                successor = self.find_min(root.right)

                root.val = successor.val

                root.right = self.deleteNode(
                    root.right,
                    successor.val
                )

        return root

    def find_min(self, root):

        current = root

        while current.left:
            current = current.left

        return current