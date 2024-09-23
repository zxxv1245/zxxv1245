H, W = map(int, input().split())
arr = [list(map(str, input())) for _ in range(H)]

dc = [1, -1]

for r in range(H):
    for c in range(W):
        if arr[r][c] == 'c':
            arr[r][c] = 0
            for power in range(1, W):
                nc = c + 1 * power
                if nc < W and arr[r][nc] == '.':
                    if arr[r][nc] != 'c':
                        arr[r][nc] = power

for r in range(H) :
    for c in range(W) :
        if arr[r][c] == '.' :
            arr[r][c] = -1


for i in arr :
    print(*i)

