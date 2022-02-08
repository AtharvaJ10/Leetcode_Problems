class Solution(object):
    def rangeSumBST(self, root, L, R):
        def dfs(node):
            if node:
                if L<= node.val <= R:
                    self.ans += node.val
                    #print(node.val)
                if node.val>L:
                    dfs(node.left)
                if node.val<R:
                    dfs(node.right)
        self.ans = 0
        dfs(root)
        return self.ans