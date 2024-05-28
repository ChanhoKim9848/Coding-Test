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

# Sort the boxTypes array in descending order by the number of units per box.
# this ensures that you prioritize boxes with the highest units first.
# iterate through the array and get two elements from each element of it.
# If the truck can carry all boxes of the current type (truckSize >= numberOfBoxes), add total units (size * unit) to res
# If the truck cannot carry all boxes of the current type (truckSize < numberOfBoxes), add only as many boxes as the truck can carry and stop.
# return res

# time complexity is O(N), The time complexity of your solution is actually O(N log N). This is because the sorting step (boxTypes.sort(key=lambda x: -x[1]))
# space complexity is O(1), as we use a constant amount of extra space regardless of the input size.
    




            




        
