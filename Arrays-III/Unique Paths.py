class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        distance = m + n -2
        r = m - 1
        nways = 1
        for i in range(1, r+1):
            nways = nways * (distance -r + i) / i
        
        return int(nways)