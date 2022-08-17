from collections import deque
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        queue = deque([])
        indegree = [0 for i in range(numCourses)]
        graph = defaultdict(list)
        for i in prerequisites:
            graph[i[1]].append(i[0])
            indegree[i[0]]+=1
        
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)
        
        while queue:
            curr = queue.popleft()
            numCourses-=1
            for node in graph[curr]:
                indegree[node]-=1
                if indegree[node]==0:
                    queue.append(node)
                    
        if numCourses:
            return False
        return True
            