import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        heap = []
        tasks = sorted([(tasks[i][0], tasks[i][1],i) for i in range(len(tasks))])
        time = tasks[0][0]
        i = 0
        res = []
        while len(res)<len(tasks):
            while i<len(tasks) and tasks[i][0]<=time:
                heapq.heappush(heap, [tasks[i][1], tasks[i][2]])
                i+=1
            if heap:
                t_diff, index = heapq.heappop(heap)
                time+=t_diff
                res.append(index)
            elif i<len(tasks):
                time = tasks[i][0]
        return res