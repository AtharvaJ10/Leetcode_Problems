class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def bfs(start, dest):
            if start not in graph or dest not in graph:
                return -1
            queue = deque([])
            queue.append([start, 1.0])
            visited = set([start])
            while queue:
                node, val = queue.popleft()
                if node==dest:
                    return val
                for i in graph[node]:
                    if i not in visited:
                        visited.add(i)
                        queue.append([i, val*graph[node][i]])
            return -1
        
        
        graph = defaultdict(dict)
        for eq,v in zip(equations, values):
            graph[eq[0]][eq[1]] = v
            graph[eq[1]][eq[0]] = 1/v
            
        res = []
        for i,j in queries:
            res.append(bfs(i,j))
        return res