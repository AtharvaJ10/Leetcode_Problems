class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [(tasks[i][0], tasks[i][1], i) for i in range(len(tasks))]
        tasks = sorted(tasks)
        
        time = tasks[0][0]
        heap = []
        res=[]
        i = 0
        while len(res)!=len(tasks):
            while i<len(tasks) and tasks[i][0]<=time:
                heapq.heappush(heap, (tasks[i][1], tasks[i][2]))
                i+=1
            
            if heap:
                proc_time, index = heapq.heappop(heap)
                time+=proc_time
                res.append(index)
            else:
                time = tasks[i][0]
        return res
        