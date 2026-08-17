# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        queue=deque([root])
        parent={root:None}
        while queue:
            node=queue.popleft()
            if node.left:
                queue.append(node.left)
                parent[node.left]=node
            if node.right:
                queue.append(node.right)
                parent[node.right]=node
            if p in parent and q in parent:
                break
        ancestors=set()
        while p:
            ancestors.add(p)
            p=parent[p]
        while q:
            if q in ancestors:
                return q
            q=parent[q]
        pointer1,pointer2=p,q
        while pointer1 != pointer2:
            pointer1=parent[pointer1] if pointer1 else q
            pointer2=parent[pointer2] if pointer2 else p
        return pointer1