n = str(input())
m = n.split('-')

answer = 0
# 첫번째는 -로 시작할 경우의 수가 있어서 따로 작업
x = sum(map(int, (m[0].split('+'))))
if n[0] == '-':
    answer -= x
else:
    answer += x

for x in m[1:]: # 첫번째 작업은 이미 했기때문에 인덱스 1부터 시작
    x = sum(map(int, (x.split('+'))))
    answer -= x
print(answer)

# m = '55-50+40'
# print(m.split('-'))
# 출력 : ['55','50+40']

# m = '10+20+30+40'
# print(m.split('-'))
# 출력 : ['10+20+30+40']

# m = '00009-00009'
# print(m.split('-'))
# 출력 : ['00009','00009']

# m = '-40+20-30'
# print(m.split('-'))
# 출력 : ['40+20','30']

# x = m.split('+') # '+'를 기준으로 끊기
# x = map(int, x) # 리스트 내의 수를 전부 정수화 하기
# x = sum(x) # 리스트 안의 있는 모든 수의 합을 출력
