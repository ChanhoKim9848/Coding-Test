class Solution(object):
    def minMaxDifference(self, num):

        num=str(num)
        i=0
        while num[i]=='9' and i<len(num)-1:
            i+=1
        return int(num.replace(num[i],'9'))-int(num.replace(num[0],'0'))

print(Solution.minMaxDifference(Solution,'99999'))


# This code aims to find the difference between the maximum and minimum numbers that can be obtained
# by replacing one digit of a given number.
# 1. Convert the input number to a string to enable easy manipulation of its digits.
# 2. Iterate through the digits of the number to identify a digit that is not already '9'.
# This digit will be replaced to achieve the maximum number.
# 3. Replace the identified digit with '9' to obtain the maximum possible number.
# 4. For the minimum possible number, replace the first digit of the number with '0'.
# 5. Calculate the difference between the maximum and minimum numbers.
# 6. Return the calculated difference.
                

        

