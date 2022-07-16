class Solution:
    def findOrder(self, N, P):
        G, indegree, ans = defaultdict(list), [0]*N, []
        for nxt, pre in P:
            G[pre].append(nxt)
            indegree[nxt] += 1
        
        def dfs(cur):
            ans.append(cur)
            indegree[cur] = -1
            for nextCourse in G[cur]:
                indegree[nextCourse] -= 1
                if indegree[nextCourse] == 0: 
                    dfs(nextCourse)            
        for i in range(N):
            if indegree[i] == 0:
                dfs(i)

        return ans if len(ans) == N else []