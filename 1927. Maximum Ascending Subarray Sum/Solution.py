class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n = len(nums)
        sum = nums[0]
        max = sum
        for i in range(1,n):
            if nums[i] > nums[i-1]:
                sum += nums[i] 
            else:
                sum = nums[i]
            if max < sum:
                max = sum
            #sum = 0
        return max