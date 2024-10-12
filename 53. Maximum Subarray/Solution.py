class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max = nums[0]
        
        if n == 0:
            return []

        sum = 0
        for i in range(n):
            sum = sum + nums[i]

            if sum > max:
                max = sum  
            
            if sum < 0:
                sum = 0
        
        return max


#https://youtu.be/AHZpyENo7k4