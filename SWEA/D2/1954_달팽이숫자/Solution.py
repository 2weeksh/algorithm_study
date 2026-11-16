import os
import sys

# 로컬에서는 같은 폴더의 input.txt를 입력으로 사용 (SWEA 서버엔 파일이 없어서 그대로 제출해도 됨)
_input_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")
if os.path.exists(_input_path):
    sys.stdin = open(_input_path, "r", encoding="utf-8")

input = sys.stdin.readline

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    maps = [[0]*N for _ in range(N)]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    x, y = 0, 0
    count = 1
    maps[y][x] = count
    dir = 0

    while count < N*N:
        n = dir%4
        nx = x + dx[n]
        ny = y + dy[n]

        if not (0<=nx<len(maps[0]) and 0<=ny<len(maps) and maps[ny][nx] == 0):
            dir += 1
            n = dir%4
            nx = x + dx[n]
            ny = y + dy[n]

        count += 1
        x, y = nx, ny
        maps[ny][nx] = count

    print(f"#{test_case}")
    for i in range(N):
        print(*maps[i])