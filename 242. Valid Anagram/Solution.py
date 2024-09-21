class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        so = sorted(s)
        to = sorted(t)
        return so == to