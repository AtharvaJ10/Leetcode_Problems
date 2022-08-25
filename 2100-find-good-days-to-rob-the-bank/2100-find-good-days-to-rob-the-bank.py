class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        if time==0:
            return list(range(len(security)))
        
        left = [0]
        temp = 0
        for i in range(1, len(security)):
            if security[i]<=security[i-1]:
                temp+=1
            else:
                temp = 0
            left.append(temp)
        
        right = [0]
        temp = 0
        for i in range(len(security)-2,-1,-1):
            if security[i]<=security[i+1]:
                temp+=1
            else:
                temp = 0
            right.append(temp)
        right = right[::-1]
        
        res=[i for i in range(len(security)) if left[i]>=time and right[i]>=time]
        return res