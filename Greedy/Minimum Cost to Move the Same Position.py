class Solution(object):
    def minCostToMoveChips(self, position):
        even=odd=0
        for i in position:
            if i%2==0:
                even+=1
            else:odd+=1
        return min(odd,even)

        # even -> odd
        # odd -> even     take 1 
        # even -> even, odd-> odd free

        
        