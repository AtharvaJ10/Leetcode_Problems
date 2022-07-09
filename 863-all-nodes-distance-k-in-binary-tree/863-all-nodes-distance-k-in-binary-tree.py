# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(parent, child):
            if parent and child:
                conn[parent.val].append(child.val)
                conn[child.val].append(parent.val)
            if child.left:
                dfs(child, child.left)
            if child.right:
                dfs(child, child.right)
        
        conn = defaultdict(list)
        dfs(None, root)
        
        queue = [target.val]
        visited = set(queue)
        for i in range(k):
            new_level = []
            for j in queue:
                for k in conn[j]:
                    if k not in visited:
                        new_level.append(k)
            queue = new_level
            visited |= set(queue)
        return queue