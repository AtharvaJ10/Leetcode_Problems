class Solution:
    def myAtoi(self, s: str) -> int:
        max1 = 2**31-1
        min1 = -2**31
        s = s.strip()
        sign = 1
        if not s:
            return 0
        
        if s[0]=="-":
            sign = -1
            
        num = 0
        i = 0
        if s[0] in ["+","-"]:
            i+=1
        while i<len(s) and s[i].isdigit():
            new_num = ord(s[i]) - ord("0")
            if num>max1 or num*10+new_num>max1:
                return max1 if sign>0 else min1
            num = num*10+new_num
            i+=1
        
        return sign*num