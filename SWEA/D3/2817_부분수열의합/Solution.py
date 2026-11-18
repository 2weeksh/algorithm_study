import os
import sys

# 로컬에서는 같은 폴더의 input.txt를 입력으로 사용 (SWEA 서버엔 파일이 없어서 그대로 제출해도 됨)
_input_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")
if os.path.exists(_input_path):
    sys.stdin = open(_input_path, "r", encoding="utf-8")

input = sys.stdin.readline

def DFS(i, arr, total):
    if total > K:
        return 0
    if i == N:
        if total == K:
            return 1
        return 0

    # i 인덱스 부분 원소 선택 안할 때
    a = DFS(i+1, arr, total)

    # i 인덱스 부분 원소 선택 할 때
    b = DFS(i+1, arr, total+arr[i])

    return a+b

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    answer = DFS(0, arr, 0)

    print(f"#{test_case} {answer}")