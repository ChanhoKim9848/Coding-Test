class Solution(object):
    def minimumSum(self, num):
# Convert 'num' array to a string and sort it in ascending order.
# Initialize pointers 'i' and 'j' at the start and end of the sorted list, respectively.
# Iterate until 'i' exceeds 'j'.
# 'res' holds the resulting value to be returned.
# 'i' represents the minimum value in the array, and 'j' represents the maximum.
# Concatenate and convert 'i' and 'j' to an integer value.
# Add each integer value to 'res' while 'i' and 'j' move inward, repeating the process.
        num = sorted(str(num))
        i, j = 0, len(num) - 1
        res = 0
        while i<j:
            res += int(num[i] + num[j])
            i+=1
            j-=1
        return res
    
# Overall, the code sorts the digits of the input number,
# then sums up the minimum pairs formed 
# by iterating through the sorted digits
# from both ends towards the middle of the list.




print(Solution.minimumSum(Solution,'2927'))
        



