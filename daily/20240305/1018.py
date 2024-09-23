N, M = map(int, input().split())

lst = [list(input()) for _ in range(N)]
minV = 21e8
for i in range(N - 7):
    for j in range(M - 7):
        cnt = 0
        for x in range(i, i + 8):
            if x % 2 == 0:
                for y in range(j, j + 8, 2):
                    if lst[x][y] != 'W':
                        cnt += 1
                for y in range(j + 1, j + 8, 2):
                    if lst[x][y] != 'B':
                        cnt += 1
            elif x % 2 == 1:
                for y in range(j, j + 8, 2):
                    if lst[x][y] != 'B':
                        cnt += 1
                for y in range(j + 1, j + 8, 2):
                    if lst[x][y] != 'W':
                        cnt += 1

        if minV > cnt:
            minV = cnt

        cnt = 0
        for x in range(i, i + 8):
            if x % 2 == 0:
                for y in range(j, j + 8, 2):
                    if lst[x][y] != 'B':
                        cnt += 1
                for y in range(j + 1, j + 8, 2):
                    if lst[x][y] != 'W':
                        cnt += 1
            elif x % 2 == 1:
                for y in range(j, j + 8, 2):
                    if lst[x][y] != 'W':
                        cnt += 1
                for y in range(j + 1, j + 8, 2):
                    if lst[x][y] != 'B':
                        cnt += 1

        if minV > cnt:
            minV = cnt

print(minV)
