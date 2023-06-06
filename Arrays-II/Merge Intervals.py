class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        out = []
        for i in range(len(intervals)):
            if out and intervals[i][0] <= out[-1][1]:
                out[-1][1] = max(out[-1][1], intervals[i][1])
            else:
                out.append(intervals[i])
        return out