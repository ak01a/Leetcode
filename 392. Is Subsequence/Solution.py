class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(t)
        m = len(s)
        i,j = 0,0
        while j<n and i<m:
            if s[i] == t[j]:
                i+=1
            j+=1
        return i==m

