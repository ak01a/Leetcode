class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        arr=[]
        for i in range(n):
            sums = 0
            for j in range(i,n):
                sums += nums[j]
                arr.append(sums)
        sum1= 0
        arr.sort()
        for i in range(left-1,right):
            sum1 += arr[i]
        
        mod = 10**9+7
        sum2 = sum1 % mod

        return sum2
        
            

