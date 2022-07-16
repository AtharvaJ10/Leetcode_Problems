from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        indegree = [0 for _ in range(numCourses)]
        
        for i in prerequisites:
            graph[i[1]].append(i[0])
            indegree[i[0]]+=1
        
        queue = deque()
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)
                
        res = []
        while queue:
            course = queue.popleft()
            for i in graph[course]:
                indegree[i]-=1
                if indegree[i]==0:
                    queue.append(i)
            res.append(course)
        
        return res if len(res)==numCourses else []

            
        
            