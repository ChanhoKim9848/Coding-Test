class Solution(object):
    def minimumBoxes(self, apple, capacity):
        s=sum(apple)
        capacity.sort()
        i=0
        while s>0:
            i+=1
            s-=capacity[-i]
        return i
    
print(Solution.minimumBoxes(Solution,[1,3,2],[4,3,1,5,2]))
