class Solution:
    def largestVariance(self, s: str) -> int:
        def kadane(array):
            res, current = 0,0
            seen = False
            for i in array:
                if i==-1:
                    seen = True
                current+=i
                if seen:
                    res = max(res, current)
                else:
                    res = max(res, current-1)
                if current<0:
                    current = 0
                    seen = False
            return res
        
        set1 = set(s)
        str1 = ''.join(set1)
        
        variance = 0
        for i in range(len(str1)-1):
            for j in range(i+1, len(str1)):
                x = str1[i]
                y = str1[j]
                temp = []
                for k in s:
                    if k!=x and k!=y:
                        continue
                    elif k==x:
                        temp.append(1)
                    else:
                        temp.append(-1)
                variance = max(variance, kadane(temp), kadane([-x for x in temp]))
        return variance