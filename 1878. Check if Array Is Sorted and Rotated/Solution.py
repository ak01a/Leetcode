class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        start_index = 0
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                start_index = i+1
                break

        for i in range(n-1):
            cur_index = (start_index + i) % n
            if nums[cur_index] > nums[(start_index + i + 1) % n]:
                return False
              
        return True