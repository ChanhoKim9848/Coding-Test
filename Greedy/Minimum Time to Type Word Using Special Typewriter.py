class Solution(object):
    def minTimeToType(self, word):
        p='a'
        res=len(word)
        for i in word:
            dif=abs(ord(i)-ord(p))
            res+=min(26-dif,dif)
            p=i
        return res
    
# p points 'a'
# res starts with the length of word as we have to type each charater
# we loop through the word string
# Calculate the absolute difference between the current character and the pointer position
# Increment the result by the minimum number of seconds required to move the pointer
# either clockwise or counterclockwise to reach the current character
# and p points i
# return res

# time complexity O(N) looping through word
# space complexity O(1)  The algorithm only uses a constant amount of 
# extra space regardless of the size of the input word. 
# It doesn't utilize any data structures that grow with the input size.

        