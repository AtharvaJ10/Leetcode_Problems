class Solution:
    def nextGreaterElement(self, n: int) -> int:
        l = list(str(n))
        
        j = len(l)-2
        while j>=0:
            if l[j]>=l[j+1]:
                j-=1
            else:
                break
        
        if j==-1:
            return -1
        
        num = l[j]
        i = j
        while i+1<len(l) and l[i+1]>l[j]:
            i+=1
        l[i],l[j] = l[j],l[i]
        l[j+1:] = l[j+1:][::-1]
        res = int(''.join(l))
        return res if res<1<<31 else -1
        
        