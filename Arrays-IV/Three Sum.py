class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        for i in range(len(nums) - 1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            mid = i + 1
            right = len(nums) - 1
            while mid < right:
                sum = nums[i] + nums[mid] + nums[right]
                if sum == 0:
                    out.append([nums[i], nums[mid], nums[right]])
                    mid += 1
                    right -= 1
                    while mid < right and nums[right] == nums[right + 1]:
                        right -= 1
                    while mid < right and nums[mid] == nums[mid - 1]:
                        mid += 1    
                elif sum > 0:
                    right -= 1
                else:
                    mid += 1
        return out