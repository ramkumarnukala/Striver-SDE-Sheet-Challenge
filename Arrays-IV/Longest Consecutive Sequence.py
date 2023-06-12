class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set()
        for i in nums:
            hashset.add(i)
        maxout = 0
        for i in nums:
            if (i-1) not in hashset:
                cur = 1
                curNum = i
                while (curNum+1) in hashset:
                    curNum += 1
                    cur += 1
                maxout = max(maxout, cur)
        return maxout