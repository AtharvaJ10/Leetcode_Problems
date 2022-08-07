class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        """stack = []
        for i in s:
            if stack and stack[-1][0]==i:
                stack[-1][1]+=1
            else:
                stack.append([i,1])
            if stack[-1][1]==k:
                stack.pop()
        return ''.join(c*k for c,k in stack)"""
        
        i=0
        count = [0] * len(s)
        s = list(s)
        for j in range(len(s)):
            s[i] = s[j]
            if i>0 and s[i-1] == s[j]:
                count[i] = count[i-1]+1
            else:
                count[i] = 1
            if count[i]==k:
                i-=k
            i+=1
        return ''.join(s[:i])