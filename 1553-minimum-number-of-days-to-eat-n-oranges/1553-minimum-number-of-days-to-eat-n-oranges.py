class Solution:
    def minDays(self, n: int) -> int:
        # O(log n)
        dp = {0:0, 1:1}
        def dfs(n):
            if n in dp:
                return dp[n]
            
            # 1 day to divide and min of number of days to be perfectly divide by 2(n%2) + divide n//2, similarly for 3
            dp[n] = 1+min(n%2 + dfs(n//2), n%3 + dfs(n//3))
            return dp[n]
        return dfs(n)