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


# Initialization: res = [] initializes an empty list called res.
# This list will store all numbers after removing the specified digit.

# Iteration: for i in range(len(number)):
# iterates over each index of the input number.

# Condition: if number[i] == digit: 
# checks if the current digit in the number matches the digit to be removed.

# Digit Removal: res.append(number[:i] + number[i+1:])
# removes the digit by concatenating the substring 
# before the digit (number[:i]) with the substring 
# after the digit (number[i+1:]), effectively removing the digit at index i.

# Return Maximum: return max(res) returns the maximum number from 
# the list of numbers after removing the digit. 
# Since res contains numbers as strings, 
# the max function returns the maximum string based on lexicographical order.