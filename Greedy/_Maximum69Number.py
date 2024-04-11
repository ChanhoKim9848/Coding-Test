class Solution(object):
    def maximum69Number (self, num):
        return int(str(num).replace('6','9',1))
    
print(Solution.maximum69Number(Solution,9996))