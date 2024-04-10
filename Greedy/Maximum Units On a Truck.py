class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        sorted_boxTypes=[]
        res=0

        for n,unit in boxTypes:
            sorted_boxTypes.append([unit,n])
        sorted_boxTypes.sort(reverse=True)
        for unit,n in sorted_boxTypes:
            if truckSize-n >=0:
                truckSize-=n
                res+=n*unit
            else:
                res+=truckSize*unit
                return res
        return res
        




            




        
