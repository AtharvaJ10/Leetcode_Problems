class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text2)> len(text1):
            text1, text2 = text2, text1
        dp = [0] * (len(text2) + 1)
        for c in text1:
            prevRow, prevRowPrevCol = 0, 0
            for j, d in enumerate(text2):
                prevRow, prevRowPrevCol = dp[j + 1], prevRow
                dp[j + 1] = prevRowPrevCol + 1 if c == d else max(dp[j], prevRow)
        return dp[-1]