class Solution(object):
    def maximum69Number (self, num):
        num=str(num)
        a=''
        i=0
        while i<len(num):
            if num[i]=='6':
                a+='9'
                for j in range(i+1,len(num)):
                    a+=num[j]
                break
            else:
                a+='9'
                i+=1
        return int(a)


# time complexity: O(N)
# space complexity: O(N)

# first we change num to str variable
# we loop through num
# if a is not 6 then we concatenate '9' to variable a
# once '6' is found, we concatenate the rest of digits
print(Solution.maximum69Number(Solution,9996))

