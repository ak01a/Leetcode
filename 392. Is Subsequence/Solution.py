class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(t)
        m = len(s)
        j = 0
        i = 0
        while j<n and i<m:
            if s[i] == t[j]:
                j+=1
                i+=1
            else:
                j+=1

        if i == m:
            return True
        else:
            return False


