class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        nn = abs(n)

        if n == 0:
            return 1
        
        while nn > 0:
            if nn % 2 == 0:
                x *= x
                nn = nn/2
            else:
                ans *= x
                nn -= 1
        
        if(n < 0):
            ans = 1 / ans
        
        return ans