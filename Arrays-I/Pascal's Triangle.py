class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        out = []
        for i in range(1, numRows+1):
            row = [1]
            for j in range(1, i+1):
                if j > 1:
                    row.append((row[-1] * (i-j+1))//(j-1))
            out.append(row)
        return out
