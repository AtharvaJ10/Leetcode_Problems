class Solution:
    def largestVariance(self, s: str) -> int:
        
        def solve(array):
            seen = False
            res = 0
            sum1 = 0
            for i in range(len(array)):
                if array[i]==-1:
                    seen = True
                sum1+=array[i]
                if seen:
                    res = max(res,sum1)
                else:
                    res = max(res,sum1-1)
                if sum1<0:
                    sum1 = 0
                    seen = False
            return res
        
        
        set1 = set(s)
        str1 = ''.join(set1)
        
        res = 0
        for i in range(len(str1)-1):
            for j in range(i+1,len(str1)):
                x = str1[i]
                y = str1[j]
                array = []
                for k in s:
                    if k!=x and k!=y:
                        continue
                    elif k==x:
                        array.append(1)
                    else:
                        array.append(-1)
                res = max(res,solve(array),solve([-x for x in array]))
        return res
        