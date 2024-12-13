class Solution:
    def reverseWords(self, s: str) -> str:
        w=s.split()
        result=""
        for i in range(len(w)-1,0,-1):
            result+=w[i]+" "
        result+=w[0]
        return result
 
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