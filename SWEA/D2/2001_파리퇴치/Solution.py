import os
import sys

# 로컬에서는 같은 폴더의 input.txt를 입력으로 사용 (SWEA 서버엔 파일이 없어서 그대로 제출해도 됨)
_input_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")
if os.path.exists(_input_path):
    sys.stdin = open(_input_path, "r", encoding="utf-8")

input = sys.stdin.readline

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_total = 0
    for r in range(N-(M-1)):
        for c in range(N-(M-1)):

            current_total = 0
            for y in range(M):
                for x in range(M):
                    current_total += arr[r+y][c+x]

            max_total =  max(max_total, current_total)

    print(f"#{test_case} {max_total}")    
