# N=3, 10 15 50 일 경우
# 로프 3개를 이용할 경우 10*3 = 30 
# 로프 2개를 이용할 경우 15*2 = 30
# 로프 1개를 이용할 경우 50*1 = 50
# 최대 반환 = 50
# for loop문을 이용해서 한 요소마다 곱해줘서 최대를 반환
N=int(input())
a=[]
for i in range(N):
    a.append(int(input()))
a.sort()
for i in range(N):
    a[i]=(N-i)*a[i]
print(max(a))