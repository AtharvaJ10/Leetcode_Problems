class Solution:
    def largestVariance(self, s: str) -> int:
        def kadane(array):
            seen = False
            res, sum1 = 0, 0
            for i in array:
                if i== -1:
                    seen = True
                sum1+=i
                if seen:
                    res = max(res, sum1)
                else:
                    res = max(res, sum1-1)
                if sum1<0:
                    sum1 = 0
                    seen = False
            return res
        
        str1 = set(s)
        str1 = ''.join(str1)
        res = 0
        for i in range(len(str1)-1):
            for j in range(i+1,len(str1)):
                x,y = str1[i], str1[j]
                array = []
                for k in s:
                    if k!=x and k!=y:
                        continue
                    elif k==x:
                        array.append(1)
                    else:
                        array.append(-1)
                print(array)
                res = max(res, kadane(array), kadane([-x for x in array]))
        return res