import os
import sys
from collections import deque

# 로컬에서는 같은 폴더의 input.txt를 입력으로 사용 (SWEA 서버엔 파일이 없어서 그대로 제출해도 됨)
_input_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")
if os.path.exists(_input_path):
    sys.stdin = open(_input_path, "r", encoding="utf-8")

input = sys.stdin.readline

T = 10
for test_case in range(1, T + 1):
    test_case = int(input())
    maps = [list(map(int, input().strip())) for _ in range(16)]
    visited = [[False]*16 for _ in range(16)]

    # 상 하 좌 우
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    # 시작 인덱스
    x, y = 1, 1
    queue = deque()
    queue.append((y, x))
    visited[y][x] = True
    complete = False

    while queue and not complete:
        y, x = queue.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if maps[ny][nx]==3:
                complete = True

            if maps[ny][nx]==0 and not visited[ny][nx]:
                queue.append((ny, nx))
                visited[ny][nx] = True

    if complete:
        answer = 1
    else: answer = 0

    print(f"#{test_case} {answer}")