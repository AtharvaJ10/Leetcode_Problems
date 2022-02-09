class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        count = 0
        
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
            elif stack and s[i]==')':
                stack.pop()
            else:
                count+=1
        
        count+=len(stack)
        return count
        