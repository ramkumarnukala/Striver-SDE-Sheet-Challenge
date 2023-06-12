class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = set()

        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 2):
                
                l = j + 1
                r = len(nums) - 1
                while(l < r):
                    temp = nums[i] + nums[j] + nums[l] + nums[r]

                    if temp == target:
                        res.add(tuple(sorted([nums[i], nums[j], nums[l], nums[r]])))
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                    elif temp > target:
                        r -= 1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
                    else:
                        l += 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1

        return res