from collections import deque
class Solution:
    def constrainedSubsetSum(self, A: List[int], k: int) -> int:
        deque = collections.deque() 
        for i in range(len(A)):
            # deque[0] is the max of (0, dp[i - k], dp[i-k+1], .., dp[i - 1])
            A[i] += deque[0] if deque else 0 
            # 1. We always want to retrieve the max of (0, dp[i - k], dp[i-k+1], .., dp[i - 1]) from `deque`
            # 2. We expect dp[i] to be added to `deque` so that we can compute dp[i + 1] in the next iteration
            # 3. So, if dp[i] is larger than some old values, we can discard them safely.
            # 4. As a result, the length of `deque` is not necessarily `k`
            while len(deque) and A[i] > deque[-1]:
                deque.pop()
            # no need to store the negative value
            if A[i] > 0:
                deque.append(A[i])
            # we do not need the value of A[i - k] when computing dp[i+1] in the next iteration, because `j - i <= k` has to be satisfied.
            if i >= k and deque and deque[0] == A[i - k]:
                deque.popleft()
        return max(A)