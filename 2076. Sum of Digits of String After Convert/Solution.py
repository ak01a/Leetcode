class Solution:
    def getLucky(self, s: str, k: int) -> int:
        su = 0
        for ch in s:
            n = ord(ch)-96
            if(n>=10):
                n = str(n)
                n1 = int(n[0:1])
                n2 = int(n[1:2])
                n = n1+n2
            su += n
        for i in range(k-1):
            if(su>=10):
                j = 0
                n = 0
                while(len(str(su))):
                    if str(su)[j:j+1]!='':
                        n += int(str(su)[j:j+1])
                        j+=1
                    else:
                        break
                su = n
            else:
                break
        return su