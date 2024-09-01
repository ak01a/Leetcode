class Solution:
    def construct2DArray(self, ori: List[int], m: int, n: int) -> List[List[int]]:
        if len(ori) != m*n:
            return [] 
        res = []
        for r in range(m):
            start = r * n
            end = start + n
            res.append(ori[start:end])

        return res