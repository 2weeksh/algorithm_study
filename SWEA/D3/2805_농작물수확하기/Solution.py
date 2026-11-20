#import sys
#sys.stdin = open(r"", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    maps = [list(map(int, input().strip())) for _ in range(N)]

    total = 0

    center = N // 2  # 2

    for y in range(N):
        if y < N//2:
            total += sum(maps[y][center-y:center+y+1])
        elif y == N//2:
            total += sum(maps[y])
        else: #y >= N//2
            total += sum(maps[y][y-center:N-y+center])

    print(f"#{test_case} {total}")


