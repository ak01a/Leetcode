class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:
        l,r = 0,len(num)-1
        while l<r:
            curSum = num[l] + num[r] 
            if curSum == target:
                return l+1,r+1
            elif curSum > target:
                r-=1
            else:
                l+=1
        return []

        