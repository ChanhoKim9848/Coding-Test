class Solution(object):
    def balancedStringSplit(self, s: str) -> int:
        res=c=0

        for i in s:
            c+=1 if i=='R' else -1
            if c==0:
                res+=1
        return res


print(Solution.balancedStringSplit(Solution,"RRLLRL"))