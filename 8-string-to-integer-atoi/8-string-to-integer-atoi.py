class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        
        sign = 1
        i = 0
        if s[0]=='-':
            sign = -1
            i+=1
        elif s[0]=="+":
            i+=1
        
        num = 0
        MAX = 2**31-1
        MIN = -2**31
        while i<len(s) and s[i].isdigit():
            new_num = ord(s[i]) - ord("0")
            if num>MAX or num*10+new_num>MAX:
                return MAX if sign>0 else MIN
            num = num*10+new_num
            i+=1
        return sign*num