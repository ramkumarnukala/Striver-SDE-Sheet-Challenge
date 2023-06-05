class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        flag = -1
        for i in range(len(nums)-2, -1, -1):
            if (nums[i] < nums[i+1]):
                flag = i
                break

        if flag == -1:
            nums.reverse()
            return nums

        for i in range(len(nums)-1, flag, -1):
            if (nums[i] > nums[flag]):
                nums[i], nums[flag] = nums[flag], nums[i]
                break

        nums[flag+1:] = reversed(nums[flag+1:])
        return nums
