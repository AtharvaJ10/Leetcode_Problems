class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        stack = [[0, [0]]]
        res = []
        while stack:
            node, path = stack.pop()
            if node == len(graph)-1:
                res.append(path)
            
            for neighbor in graph[node]:
                stack.append([neighbor, path+[neighbor]])
        return res