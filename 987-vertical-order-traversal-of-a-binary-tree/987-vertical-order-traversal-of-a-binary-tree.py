# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([])
        queue.append([root,0,0])
        d = defaultdict(list)
        min1 = max1 = 0
        while queue:
            node, row, col = queue.popleft()
            d[col].append([row, node.val])
            if node.left:
                queue.append([node.left, row+1, col-1])
                min1 = min(min1, col-1)
            if node.right:
                queue.append([node.right, row+1, col+1])
                max1 = max(max1, col+1)
        
        res = []
        for i in range(min1, max1+1):
            d[i] = sorted(d[i])
            temp = []
            for j in d[i]:
                temp.append(j[1])
            res.append(temp)
        return res