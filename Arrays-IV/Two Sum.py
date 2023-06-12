class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i, value in enumerate(numbers): 
            remaining = target - numbers[i] 
           
            if remaining in seen: 
                return [seen[remaining], i]
            else:
                seen[value] = i  