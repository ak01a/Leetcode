class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # Initialize the base cases
        one, two = 1, 2
        
        # Iterate from step 3 to n
        for _ in range(3, n + 1):
            # Calculate the number of ways to reach the current step
            temp = one + two
            # Update the previous two steps
            one = two
            two = temp
        
        # The result is stored in 'two'
        return two