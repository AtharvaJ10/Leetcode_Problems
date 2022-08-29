class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0]*numCourses
        for i,j in prerequisites:
            graph[j].append(i)
            indegree[i]+=1
        
        queue = deque([])
        for i in range(numCourses):
            if indegree[i]==0:
                queue.append(i)
        
        count = 0
        while queue:
            node = queue.popleft()
            count+=1
            for nei in graph[node]:
                indegree[nei]-=1
                if indegree[nei]==0:
                    queue.append(nei)
        return True if count==numCourses else False