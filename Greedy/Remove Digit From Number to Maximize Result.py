class Solution(object):
    def removeDigit(self, number, digit):
        # Initialize an empty list to store all numbers after removing the digit
        res = []
        
        # Iterate through each digit in the number
        for i in range(len(number)):
            # If the current digit matches the digit to be removed
            if number[i] == digit:
                # Remove the digit and append the resulting number to the list
                res.append(number[:i] + number[i+1:])
        
        # Return the maximum number from the list of numbers after removing the digit
        return max(res)
    
print(Solution.removeDigit(Solution,"1231","1"))