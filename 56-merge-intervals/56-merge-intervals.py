class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key =lambda row: row[0])
        stack = []
        for i in intervals:
            if stack and i[0]<=stack[-1][1]:
                stack[-1] = [stack[-1][0], max(stack[-1][1],i[1])]
            else:
                stack.append(i)
        return stack
                