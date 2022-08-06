class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        k = 0
        current = ""
        for i in s:
            if i=="[":
                stack.append((current,k))
                current = ""
                k = 0
            elif i.isdigit():
                k = k*10 + int(i)
            elif i =="]":
                last_s, last_k = stack.pop()
                current = last_s + current*last_k
            else:
                current+=i
        return current