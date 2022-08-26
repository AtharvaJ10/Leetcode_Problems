class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        arr = self.d[key]
        low = 0
        hi = len(arr)
        while low<hi:
            mid = (low+hi)//2
            if arr[mid][0]<=timestamp:
                low = mid+1
            else:
                hi = mid
        return "" if hi==0 else arr[hi-1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)