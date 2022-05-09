class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda row: row[0])
        result = []
        for i in range(len(intervals)):
            if result and intervals[i][0]<=result[-1][1]:
                result[-1] = [result[-1][0],max(intervals[i][1],result[-1][1])]
            else:
                result.append(intervals[i])
        return result
                