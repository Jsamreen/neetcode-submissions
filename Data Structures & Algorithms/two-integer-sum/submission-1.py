class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for ind, num in enumerate(nums):
            remainder = target - num  
            if remainder in seen:
                return [seen[remainder], ind]
            seen[num]= ind
        return None
            

        