class Solution(object):
    def minimumCost(self, cost):
        cost.sort()
        return sum(cost) - sum(cost[-3::-3])


print(Solution.minimumCost(Solution, [3, 3, 3, 1]))

# cost.sort(): This sorts the cost array in ascending order.
# return sum(cost) - sum(cost[-3::-3]): This line calculates the total sum of all elements
# in the cost array and then subtracts the sum of every third element
# from the end (starting from the third-last element and moving backwards).

# Here's a step-by-step explanation of the second part of the line:
# cost[-3::-3]: This extracts every third element from the end of the sorted cost array,
# starting from the third-last element and moving backwards.
# For example, if cost is [1, 2, 3, 4, 5, 6, 7, 8, 9], cost[-3::-3] would be [7, 4, 1].
# sum(cost[-3::-3]): This calculates the sum of the elements extracted in the previous step.

# sum(cost) - sum(cost[-3::-3]): Finally, this subtracts
# the sum of every third element from the total sum of all elements in the cost array.
