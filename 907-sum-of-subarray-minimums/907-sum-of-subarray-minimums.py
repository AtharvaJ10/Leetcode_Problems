class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        res = 0
        for i in range(len(arr)+1):
            while stack and (i==len(arr) or arr[stack[-1]]>arr[i]):
                j = stack.pop()
                k = stack[-1] if stack else -1
                res+=arr[j]*(i-j)*(j-k)
            stack.append(i)
        return res%(10**9 + 7)
        