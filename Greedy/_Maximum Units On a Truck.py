class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        res=0
        boxTypes.sort(key=lambda x:-x[1])
        for n,unit in boxTypes:
            if truckSize-n >=0:
                truckSize-=n
                res+=n*unit
            else:
                res+=truckSize*unit
                break
        return res

print(Solution.maximumUnits(Solution,[[1,3],[2,2],[3,1]],4))
        
    




            




        
