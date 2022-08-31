class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        queue = deque([])
        for i in range(1, 10):
            queue.append(i)
        
        res = []
        while queue:
            num = queue.popleft()
            if low<=num<=high:
                res.append(num)
            if num>high:
                return res
            
            last = num%10
            if last<9:
                queue.append(num*10+last+1)
        return res