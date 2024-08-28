class Solution:
    #TLE
    '''
   def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums)
        for i in range(1,n):
            if nums[i] == nums[i-1]:
                return True
        return False             
    '''
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for i in nums:
            if i in s:
                return True
            else:
                s.add(i)

        return False