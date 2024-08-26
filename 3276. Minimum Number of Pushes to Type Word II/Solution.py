class Solution:
    def minimumPushes(self, word: str) -> int:
        sort=Counter(word)
        sort1=dict(sorted(sort.items(),key=lambda item: -item[1]))
        count=0
        cost=0
        for value in sort1.values():
            count+=1
            if(count>8):
                n=((count-1)//8)+1
                cost=cost+(n*value)
                continue
            else:
                cost=cost+(value)
        return cost