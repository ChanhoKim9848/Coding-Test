# Initialization:
#  The lengths of word1 and word2 are stored in len1 and len2, respectively.
#  Variables i and j are initialized to zero to track positions in both words.
#  An empty list called result is created to store the interleaved characters.

# Interleaving Characters: A while loop runs as long as both i is less than len1 and j is less than len2.

# Inside the loop:
# The character at index i from word1 and the character at index j from word2 are appended to the result list.

# Both i and j are incremented by one to move to the next character in each word.

# Appending Remaining Characters: After the loop, any remaining characters from word1 (starting from index i) and word2 (starting from index j) are appended to the result list.

# Returning the Result: Finally, the result list is joined into a single string using the join method and returned.
class Solution(object):
    def mergeAlternately(self, word1, word2):
        len1,len2=len(word1),len(word2)
        i,j=0,0
        result=[]
        while i<len1 and j<len2:
            result.append(word1[i])
            result.append(word2[j])
            i+=1
            j+=1
        result.append(word1[i:])
        result.append(word2[j:])

        return "".join(result)

        