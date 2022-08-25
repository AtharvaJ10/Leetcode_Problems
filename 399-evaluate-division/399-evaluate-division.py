from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def bfs(start, dest):
            if start not in graph and dest not in graph:
                return -1.0
            queue = [(start, 1.0)]
            visited = set()
            for x,v in queue:
                if x==dest:
                    return v
                visited.add(x)
                for j in graph[x]:
                    if j not in visited:
                        queue.append([j, v*graph[x][j]])
            return -1.0
        
        graph = defaultdict(dict)
        for eq, val in zip(equations, values):
            i,j = eq
            graph[i][j] = val
            graph[j][i] = 1/val
        
        return [bfs(i,j) for i,j in queries]
        
        """def dfs(graph, start, end, visited):
            if start == end and graph[start]:
                return 1.0
            
            visited.add(start)
            for neigh, val in graph[start]:
                if neigh in visited:
                    continue
                
                tmp = dfs(graph, neigh, end, visited)
                if tmp > 0:
                    return val * tmp
            
            return -1.0
            
        graph = collections.defaultdict(set)
        for items, v in zip(equations, values):
            x, y = items
            graph[x].add((y, v))
            graph[y].add((x, 1.0 / v))
        
        res = []
        for q in queries:
            res.append(dfs(graph, q[0], q[1], set()))
        
        return res"""