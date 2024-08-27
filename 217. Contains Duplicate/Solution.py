class Solution:
    #TLE
    '''
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(0,n):
            for j in range(i+1,n):
                if nums[i] == nums[j]:
                    return True
        return False

    '''
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums)
        for i in range(1,n):
            if nums[i] == nums[i-1]:
                return True
        return False             