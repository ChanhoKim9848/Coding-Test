import sys
input = sys.stdin.readline

# 강의를 끝나는 시간 기준으로 오름차순으로 정렬
# for loop으로 이전 강의의 끝나는 시간이 새로 시작하는 강의 시간 보다 같거나 작으면 카운트
result=0
previous=0
n=int(input())
times=[]
for i in range(n):
    times.append(list(map(int,input().split())))

times.sort(key=lambda x: (x[1],x[0]))

for start,end in times:
    
    if previous <= start:
        result+=1
        previous = end
print(result)

# O(n log n)