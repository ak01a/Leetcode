class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0]
        for num in nums:
            if abs(closest) > abs(num):
                closest = num
            elif abs(closest) == abs(num) and num > closest:
                closest = num
        return closest