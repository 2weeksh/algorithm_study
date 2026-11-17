import os
import sys

# 로컬에서는 같은 폴더의 input.txt를 입력으로 사용 (SWEA 서버엔 파일이 없어서 그대로 제출해도 됨)
_input_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")
if os.path.exists(_input_path):
    sys.stdin = open(_input_path, "r", encoding="utf-8")

input = sys.stdin.readline


def rotate90(maps):
    rotate_90 = [list(row) for row in zip(*maps[::-1])]
    return rotate_90

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    maps = [list(map(int, input().split())) for _ in range(N)]

    rotate90_maps = rotate90(maps)
    rotate180_maps = rotate90(rotate90_maps)
    rotate270_maps = rotate90(rotate180_maps)

    print(f"#{test_case}")
    for i in range(N):
        result = "".join(map(str, rotate90_maps[i]))+" "+"".join(map(str, rotate180_maps[i]))+" "+"".join(map(str, rotate270_maps[i]))
        print(result)