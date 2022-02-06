class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = [""] * len(s)
        stack = []
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            elif s[i] >= 'a' and s[i]<='z':
                res[i] = s[i]
            else:
                if stack!=[]:
                    res[stack.pop()] = '('
                    res[i] = ')'
        return ''.join(res)
                