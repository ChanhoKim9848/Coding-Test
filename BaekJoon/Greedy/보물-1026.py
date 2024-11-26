n=int(input())
A=sorted(map(int,input().split()))
B=sorted(map(int,input().split()))[::-1]
result=0
for i in range(n):
    result+=A[i]*B[i]
print(result)
