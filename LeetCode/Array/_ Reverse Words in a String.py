class Solution(object):
    def reverseWords(self, s):
        return " ".join(s.split()[::-1])

    # result,i,n = '' , 0 , len(s)
    #     while i<n:
    #         while i<n and s[i] == ' ':i+=1
    #         if i >= n: break
    #         j=i+1
    #         while j<n and s[j]!=' ': j+=1
    #         substring = s[i:j]
    #         if len(result) == 0: result = substring
    #         else: result = substring + ' ' + result
    #         i = j+1
    #     return result