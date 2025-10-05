def solution(board, moves):
    stack = []
    answer = 0

    for m in moves:
        for i in range(len(board)):  # 행 길이만큼 반복
            if board[i][m-1] != 0:   # 인형 발견!
                doll = board[i][m-1]  # 인형 번호 저장
                board[i][m-1] = 0     # 꺼낸 자리는 비우기

                if stack and stack[-1] == doll:
                    stack.pop()
                    answer += 2       # 터진 인형 개수 누적
                else:
                    stack.append(doll)
                break  # 한 열에서 하나만 뽑고 다음 move로

    return answer
