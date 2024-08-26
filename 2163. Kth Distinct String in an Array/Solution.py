class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        x = Counter(arr)
        arr2 = []
        for i in x:
            if x[i] == 1:
                arr2.append(i)
        if k > len(arr2):
            return ""
        else:
            return arr2[k-1]
