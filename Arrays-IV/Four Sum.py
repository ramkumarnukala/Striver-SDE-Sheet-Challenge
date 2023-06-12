class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        out = set()
        n = len(nums)
        
        for i in range(n):
            for j in range(i+1, n):
                hashset = set()
                for k in range(j+1, n):
                    tot = nums[i] + nums[j] + nums[k]
                    t = target - tot
                    if t in hashset:
                        temp = [nums[i], nums[j], nums[k], t]
                        temp.sort()
                        out.add(tuple(temp))
                    hashset.add(nums[k])
        
        ans = [list(t) for t in out]
        return ans