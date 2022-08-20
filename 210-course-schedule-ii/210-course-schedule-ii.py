from collections import deque
from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0 for i in range(numCourses)]
        for i,j in prerequisites:
            graph[j].append(i)
            indegree[i]+=1
        
        queue = deque([])
        for i in range(len(indegree)):
            if indegree[i]==0:
                queue.append(i)
        
        res = []
        while queue:
            node = queue.popleft()
            res.append(node)
            
            for req in graph[node]:
                indegree[req]-=1
                if indegree[req]==0:
                    queue.append(req)
        
        return res if len(res)==numCourses else []