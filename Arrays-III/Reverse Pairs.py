class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def mergeSort(nums, low, high):
            if low >= high:
                return 0
            mid = (low + high) // 2
            inv = mergeSort(nums, low, mid)
            inv += mergeSort(nums, mid + 1, high)
            inv += merge(nums, low, mid, high)
            return inv


        def merge(nums, low, mid, high):
            total = 0
            j = mid + 1
            for i in range(low, mid + 1):
                while j <= high and nums[i] > 2 * nums[j]:
                    j += 1
                total += (j - (mid + 1))
            t = []
            left = low
            right = mid + 1
            while left <= mid and right <= high:
                if nums[left] <= nums[right]:
                    t.append(nums[left])
                    left += 1
                else:
                    t.append(nums[right])
                    right += 1
            while left <= mid:
                t.append(nums[left])
                left += 1
            while right <= high:
                t.append(nums[right])
                right += 1
            for i in range(low, high + 1):
                nums[i] = t[i - low]
            return total


        return mergeSort(nums, 0, len(nums) - 1)