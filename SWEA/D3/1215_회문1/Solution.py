#import sys
#sys.stdin = open(r"", "r")

# 하, 우
dx = [0, 1]
dy = [1, 0]

T = 10
for test_case in range(1, T + 1):
    N = int(input())
    maps = [input().strip() for _ in range(8)]
    count = 0

    if N == 1:
        count = 64

    # 행, 열
    for y in range(8):
        for x in range(8):
            # 하, 우 방향
            for d in range(2):
                stack = []
                cy, cx = y, x
                stack.append(maps[y][x])
                # N만큼
                for i in range(1, N):
                    nx = cx + dx[d]
                    ny = cy + dy[d]

                    if not (0<=nx<8 and 0<=ny<8):
                        break

                    if N%2 == 0: #짝수 일 때
                        if i < N//2:
                            stack.append(maps[ny][nx])
                        if i >= N//2:
                            current_value = stack.pop()
                            # 다르면 바로 짤
                            if maps[ny][nx] != current_value:
                                break
                            # 값이 맞고, stack이 비어있으면 회문
                            elif maps[ny][nx] == current_value and not stack:
                                count += 1

                    else: # 홀수 일 때
                        if i < N//2:
                            stack.append(maps[ny][nx])
                        elif i > N//2:
                            current_value = stack.pop()
                            # 다르면 바로 짤
                            if maps[ny][nx] != current_value:
                                break
                            # 값이 맞고, stack이 비어있으면 회문
                            elif maps[ny][nx] == current_value and not stack:
                                count += 1


                    cy, cx = ny, nx

    print(f"#{test_case} {count}")