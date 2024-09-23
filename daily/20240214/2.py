dx = [-1, -1, -1]
dy = [-1, 0, 1]
def find(k, i, q):
    for a in range(3):
        for b in range(1, k + 1):
            nx = k + dx[a] * b
            ny = i + dy[a] * b
            if 0 <= nx < N and 0 <= ny < N and check[nx][ny] == 1:
                q = 1
                return q
    return q
def Queen(k):
    global cnt
    if k == N:
        cnt += 1
        return

    for i in range(N):
        if k >= 1:
            if find(k, i, 0) == 1:
                continue
        check[k][i] = 1
        Queen(k + 1)
        check[k][i] = 0

T = int(input())

for Test in range(1, T + 1):
    N = int(input())
    check = [[0] * N for _ in range(N)]
    cnt = 0
    Queen(0)
    print(f'#{Test} {cnt}')