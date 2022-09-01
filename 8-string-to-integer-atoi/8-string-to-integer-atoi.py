class Solution:
    def myAtoi(self, s: str) -> int:
        max1 = 2**31-1
        min1 = -2**31
        
        s = s.strip()
        sign = 1
        num = 0
        index = 0
        if not s:
            return num
        if s[0]=="-":
            sign = -1
            index+=1
        elif s[0]=="+":
            index+=1
        
        while index<len(s) and s[index].isdigit():
            curr = ord(s[index]) - ord('0')
            if (num>max1//10) or (num==max1//10 and curr>7):
                return max1 if sign==1 else min1
            num = num*10+curr
            index+=1
        
        return sign*num