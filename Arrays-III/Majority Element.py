class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        out = nums[cnt]
        for i in nums:
            if cnt == 0:
                out = i
                cnt += 1
            elif i == out:
                cnt += 1
            else:
                cnt -= 1
        cntchk = 0
        for i in nums:
            if i == out:
                cntchk += 1
        
        if cntchk > len(nums) // 2:
            return out
        return -1