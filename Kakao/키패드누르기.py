def solution(numbers, hand):
    answer = ''
    nums = {1:(0,0), 2:(0,1), 3:(0,2),
            4:(1,0), 5:(1,1), 6:(1,2),
            7:(2,0), 8:(2,1), 9:(2,2),
            '*':(3,0), 0:(3,1), '#':(3,2)}

    L, R = nums['*'], nums['#']  # 초기 손 위치

    for n in numbers:
        if nums[n][1] == 0:       # 왼쪽 열
            L = nums[n]
            answer += 'L'
        elif nums[n][1] == 2:     # 오른쪽 열
            R = nums[n]
            answer += 'R'
        else:                     # 중앙 열
            l_dist = abs(nums[n][0]-L[0]) + abs(nums[n][1]-L[1])
            r_dist = abs(nums[n][0]-R[0]) + abs(nums[n][1]-R[1])
            if l_dist < r_dist:
                L = nums[n]
                answer += 'L'
            elif l_dist > r_dist:
                R = nums[n]
                answer += 'R'
            else:
                if hand == 'left':
                    L = nums[n]
                    answer += 'L'
                else:
                    R = nums[n]
                    answer += 'R'

    return answer
