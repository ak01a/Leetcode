class Solution:
    def mySqrt(self, x: int) -> int:
        for i in range((x//2)+2):
            if i*i == x:
                return i
            elif i*i > x:
                break
        if i>1 :
            return i-1
        return 1

        