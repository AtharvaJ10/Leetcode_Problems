class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        d = defaultdict(list)
        for name, time in zip(keyName, keyTime):
            time = int(time[:2])*60 + int(time[3:])
            d[name].append(time)
        
        res = []
        for name in d:
            arr = d[name]
            arr.sort()
            for i in range(len(arr)):
                if i>1 and arr[i]-arr[i-2]<=60:
                    res.append(name)
                    break
        return sorted(res)
            