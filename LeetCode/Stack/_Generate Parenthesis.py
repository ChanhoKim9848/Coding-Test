class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        stack=[]

        def backtracking(openN,closeN):
            if openN == closeN == n:
                res.append("".join(stack))
                return
            
            if openN < n:
                stack.append('(')
                backtracking(openN+1,closeN)
                stack.pop()
            
            if openN > closeN:
                stack.append(')')
                backtracking(openN,closeN+1)
                stack.pop()
            
        backtracking(0,0)
        return res

# Time complexity O ( 4^N / N^1/2 )
# Space complexity O (N)