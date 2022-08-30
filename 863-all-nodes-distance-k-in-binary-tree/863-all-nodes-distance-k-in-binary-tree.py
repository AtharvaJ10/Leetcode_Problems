# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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
            level = []
            for j in range(len(queue)):
                for l in conn[queue[j]]:
                    if l not in visited:
                        level.append(l)
            queue = level
            visited |= set(queue)
        return queue