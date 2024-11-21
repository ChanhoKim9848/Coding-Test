N,K=map(int,input().split())
result=0
array=[]

for i in range(N):
    array.append(int(input()))
    
for i in range(N-1,-1,-1):
    if K>=array[i]:
        result+=K//array[i]
        K %= array[i]
        
        if K==0:
            break
print(result)