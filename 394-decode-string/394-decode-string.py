class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_string, k = "", 0
        for i in s:
            if i=="[":
                stack.append([current_string, k])
                current_string = ""
                k = 0
            elif i=="]":
                last_string, last_k = stack.pop()
                current_string = last_string + current_string * last_k
            elif i.isdigit():
                k = k*10+int(i)
            else:
                current_string+=i
        return current_string