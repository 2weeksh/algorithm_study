import sys
sys.stdin = open(r"C:\Users\joohy\PycharmProjects\ssafy\Sum\input.txt", "r")

T = 10
for test_case in range(1, T + 1):
    test = int(input())
    maps = [list(map(int, input().split())) for _ in range(100)]

    # 행,열 바꾼 2차원 배열
    c_maps = [list(row) for row in zip(*maps)]

    # 최대값
    values = set()

    # 대각선 값
    r_cross = 0
    l_cross = 0

    for i in range(100):
        values.add(sum(maps[i]))
        values.add(sum(c_maps[i]))

        r_cross += maps[i][i]
        l_cross += maps[i][99-i]

    values.add(r_cross)
    values.add(l_cross)

    answer = max(values)

    print(f"#{test} {answer}")