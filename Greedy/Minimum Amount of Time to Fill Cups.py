class Solution(object):
    def fillCups(self, amount):
        return max(max(amount),(sum(amount)+1)//2)
    

print(Solution.fillCups(Solution,[1,1,1]))