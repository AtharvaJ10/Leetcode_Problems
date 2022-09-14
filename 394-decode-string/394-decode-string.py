class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr, k = "",0
        res= ""
        for i in range(len(s)):
            if s[i].isdigit():
                k = k*10+int(s[i])
            elif s[i]=="[":
                stack.append([curr,k])
                k = 0
                curr = ""
            elif s[i]=="]":
                prev, temp = stack.pop()
                curr = prev + curr*temp
            else:
                curr+=s[i]
        return curr