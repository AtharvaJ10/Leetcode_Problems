class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = sorted([tasks[i][0], tasks[i][1], i] for i in range(len(tasks)))
        heap = []
        time = tasks[0][0]
        res = []
        i=0
        while len(res)!=len(tasks):
            while i<len(tasks) and tasks[i][0]<=time:
                heapq.heappush(heap, (tasks[i][1], tasks[i][2]))
                i+=1
            if heap:
                diff, ind = heapq.heappop(heap)
                time+=diff
                res.append(ind)
            else:
                time = tasks[i][0]
        return res