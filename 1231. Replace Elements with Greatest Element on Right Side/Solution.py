class Solution:
    def replaceElements(self, A: List[int],mx = -1) -> List[int]:
        for i in range(len(A)-1,-1,-1):
            A[i],mx = mx,max(A[i],mx)
        return A