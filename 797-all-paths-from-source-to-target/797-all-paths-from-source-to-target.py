class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        stack = [(0, [0])]  #Stack of Node and path
        res = []
        while stack:
            node, path = stack.pop()
            if node == len(graph)-1:   #if node is target
                res.append(path)
            
            for neighbor in graph[node]:  # Add neighbors and respective path in stack
                stack.append((neighbor, path+[neighbor]))
        return res
            