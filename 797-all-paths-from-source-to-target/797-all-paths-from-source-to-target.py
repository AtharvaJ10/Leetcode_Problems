class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        if not graph:
            return None
        
        d = {}
        for i in range(len(graph)):
            d[i] = graph[i]
        
        stack = [[0, [0]]]
        res = []
        while stack:
            node, path = stack.pop()
            if node == len(graph)-1:
                res.append(path)
            
            for i in d[node]:
                stack.append([i, path+[i]])
        return res