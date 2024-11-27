class Solution:
    def reverseWords(self, s: str) -> str:
        # s.split() splits the input string s into a list of words
        # the method without any arguments, automatically splits the string
        # by whitespace and removes extra spaces
        words=s.split()
        # creating an empty list to store the reversed words
        res=[]

        # iterating over the list in reverse order
        for i in range(len(words)-1,-1,-1):
            # a loop starts from the end of the words list
            # and goes backward until it reaches the beginning
        
            res.append(words[i])
            # since we are iterating from the end to the beginning
            # each word is added in reverse order
            if i!=0:
                res.append(" ")
            # if the current word is not the last word in the reversed list
            # we put a space between words but no trailing space at the end
        return "".join(res)

        
      # two pointers
        def reverseWords(self, s: str) -> str:
            res=[]
            words=s.split()
            i,j=0,len(words)-1

            while i<j:
                words[i],words[j]=words[j],words[i]
                i+=1
                j-=1

            return " ".join(words)