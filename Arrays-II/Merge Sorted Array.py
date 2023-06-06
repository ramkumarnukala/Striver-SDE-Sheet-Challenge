from typing import List

def swapMethod(nums1 , nums2, a, b):
    if nums1[a] > nums2[b]:
        nums1[a], nums2[b] = nums2[b], nums1[a]
        

class Solution:   
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        length = len(nums1) + len(nums2)
        gap = (length // 2) + (length % 2)

        while gap > 0:
            left = 0
            right = gap
            while right < length:
                if left >= len(nums1):
                    swapMethod(nums2 ,nums2, left - len(nums1), right - len(nums1))
                elif right < len(nums1):
                    swapMethod(nums1, nums1, left, right)
                else:
                    print()
                    swapMethod(nums1, nums2, left, right-len(nums1))
                left+=1
                right+=1

            if gap == 1:
                break
            gap = (gap // 2) + (gap % 2)
            
def main():
    obj = Solution()
    nums1=[1,2,3]
    nums2=[2,5,6]
    obj.merge(nums1, len(nums1), nums2, len(nums2))

if __name__ == "__main__":
    main()
