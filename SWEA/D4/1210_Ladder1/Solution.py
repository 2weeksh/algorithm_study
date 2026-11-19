import sys
sys.stdin = open(r"C:\Users\joohy\PycharmProjects\ssafy\Ladder1\input.txt", "r")

T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    test_count = int(input())
    maps = [list(map(int, input().split())) for _ in range(100)]

    # 도착 지점 인덱스 구하기
    for i in range(100):
        if maps[99][i] == 2:
            y, x = 99, i

    # 좌우상하
    dx = [-1, 1, 0]
    dy = [0, 0, -1]

    while True:
        # 0번째 행에 왔을 때 break
        if y == 0:
            break

        # 좌우상
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0<=nx<100 and 0<=ny<100):
                continue
            if maps[ny][nx] == 1:
                maps[y][x] += 5
                x = nx
                y = ny
                break

    print(f"#{test_count} {x}")

