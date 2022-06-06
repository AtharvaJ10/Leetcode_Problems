class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x:x[0] )
        stack = []
        for i in range(len(intervals)):
            if stack and intervals[i][0]<=stack[-1][1]:
                stack[-1] = [stack[-1][0],max(stack[-1][1],intervals[i][1])]
            else:
                stack.append([intervals[i][0],intervals[i][1]])
        return stack