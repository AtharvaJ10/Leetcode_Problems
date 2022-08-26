from collections import deque
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        queue = deque(range(1,10))
        res= []
        while queue:
            num = queue.popleft()
            if num>high:
                return res
            if low<=num<=high:
                res.append(num)
            last = num%10
            if last<9:
                queue.append(num*10+last+1)
        return res