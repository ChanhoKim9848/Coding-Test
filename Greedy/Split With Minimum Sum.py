class Solution:
    def splitNum(self, num: int) -> int:
        num="".join(sorted(str(num)))
        return int(num[::2])+int(num[1::2])
    
print(Solution.splitNum(Solution, 4325))