n=int(input())
a=list(map(int,input().split()))
a.sort()
# 1 2 3 3 4
# 1 3 6 9 13
# 32

for i in range(1,n):
    a[i]+=a[i-1]

print(sum(a))