import sys
sys.stdin = open(r"C:\Users\joohy\PycharmProjects\ssafy\battlefield\input.txt", "r")

# 상 하 좌 우
dc = [0, 0, -1, 1]
dr = [-1, 1, 0, 0]

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    H, W = map(int, input().split())
    maps = [list(input().strip()) for _ in range(H)]
    N = int(input())
    arr = input().strip()
    escape = False

    for r in range(H):
        for c in range(W):
            if maps[r][c] == '^' or maps[r][c] == 'v' or maps[r][c] == '<' or maps[r][c] == '>':
                s_r, s_c = r, c
                escape = True
                break
        if escape:
            break

    c_r = s_r
    c_c = s_c

    for i in range(N):
        if arr[i] == 'S':
            if maps[c_r][c_c] == '^':
                sim_r = c_r
                sim_c = c_c
                while True:
                    n_r = sim_r + dr[0]
                    n_c = sim_c + dc[0]
                    if not (0<=n_r<H and 0<=n_c<W):
                        break
                    if maps[n_r][n_c] == '*':
                        maps[n_r][n_c] = '.'
                        break
                    if maps[n_r][n_c] == '#':
                        break
                    sim_r = n_r
                    sim_c = n_c
            if maps[c_r][c_c] == 'v':
                sim_r = c_r
                sim_c = c_c
                while True:
                    n_r = sim_r + dr[1]
                    n_c = sim_c + dc[1]
                    if not (0 <= n_r < H and 0 <= n_c < W):
                        break
                    if maps[n_r][n_c] == '*':
                        maps[n_r][n_c] = '.'
                        break
                    if maps[n_r][n_c] == '#':
                        break
                    sim_r = n_r
                    sim_c = n_c
            if maps[c_r][c_c] == '<':
                sim_r = c_r
                sim_c = c_c
                while True:
                    n_r = sim_r + dr[2]
                    n_c = sim_c + dc[2]
                    if not (0 <= n_r < H and 0 <= n_c < W):
                        break
                    if maps[n_r][n_c] == '*':
                        maps[n_r][n_c] = '.'
                        break
                    if maps[n_r][n_c] == '#':
                        break
                    sim_r = n_r
                    sim_c = n_c
            if maps[c_r][c_c] == '>':
                sim_r = c_r
                sim_c = c_c
                while True:
                    n_r = sim_r + dr[3]
                    n_c = sim_c + dc[3]
                    if not (0 <= n_r < H and 0 <= n_c < W):
                        break
                    if maps[n_r][n_c] == '*':
                        maps[n_r][n_c] = '.'
                        break
                    if maps[n_r][n_c] == '#':
                        break
                    sim_r = n_r
                    sim_c = n_c

        if arr[i] in ('U', 'D', 'L', 'R'):
            if arr[i] == 'U':
                n_r = c_r + dr[0]
                n_c = c_c + dc[0]
                if 0 <= n_r < H and 0 <= n_c < W:
                    if maps[n_r][n_c] == '.':
                        maps[c_r][c_c] = '.'
                        c_r, c_c = n_r, n_c
                maps[c_r][c_c] = '^'

            if arr[i] == 'D':
                n_r = c_r + dr[1]
                n_c = c_c + dc[1]
                if 0 <= n_r < H and 0 <= n_c < W:
                    if maps[n_r][n_c] == '.':
                        maps[c_r][c_c] = '.'
                        c_r, c_c = n_r, n_c
                maps[c_r][c_c] = 'v'

            if arr[i] == 'L':
                n_r = c_r + dr[2]
                n_c = c_c + dc[2]
                if 0 <= n_r < H and 0 <= n_c < W:
                    if maps[n_r][n_c] == '.':
                        maps[c_r][c_c] = '.'
                        c_r, c_c = n_r, n_c
                maps[c_r][c_c] = '<'
            if arr[i] == 'R':
                n_r = c_r + dr[3]
                n_c = c_c + dc[3]
                if 0<=n_r<H and 0<=n_c<W:
                    if maps[n_r][n_c] == '.':
                        maps[c_r][c_c] = '.'
                        c_r, c_c = n_r, n_c
                maps[c_r][c_c] = '>'

    print(f"#{test_case}", end=' ')
    for i in range(H):
        print("".join(maps[i]))