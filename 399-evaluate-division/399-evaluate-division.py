class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def bfs(start, end):
            queue = deque([])
            queue.append([i,1])
            visited = set([start])
            while queue:
                start, val = queue.popleft()
                if start==j:
                    return val
                for k in graph[start]:
                    if k not in visited:
                        visited.add(k)
                        queue.append([k, val*graph[start][k]])
            return -1.0
        
        
        graph = defaultdict(dict)
        for eq,val in zip(equations, values):
            i,j = eq[0],eq[1]
            graph[i][j] = val
            graph[j][i] = 1/val
        
        res = []
        for i,j in queries:
            if i not in graph or j not in graph:
                res.append(-1.0)
                continue
            res.append(bfs(i,j))
        return res
                
            
            
                
                
        