"""
Strategy : Dynamic programming
T = O(n)

"""

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        A = [1] * n #Longest strictly increasing sub array
        for i in range(1,n):
            if nums[i] > nums[i-1]:
                A[i] += A[i-1]

        B = [1] * n #Longest strictly decrasing sub array
        for i in range(1,n):
            if nums[i] < nums[i-1]:
                B[i] += B[i-1]
            
        return max(max(A),max(B))
        
