T = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def maze(arr, n):
    for r in range(n):
        for c in range(n):
            if arr[r][c] == 2:
                sr = r
                sc = c
                break   # 시작점을 다 찾고 반복문이 그만 돌도록 해야 r,c이 시작해야하는점에서 멈춰요. 밑에서 nr,nc 찾을 때 r,c를 써야하기 때문에 시작점을 찾았으면 반복문이 그만 돌도록 해줘야해요

    stack = []
    answer = 1
    visited = [[0] * n for _ in range(n)]
    stack.append((sr, sc)) # 깊이 우선 탐색을 하여 다시 돌아와야하는데 시작점이 없으면 돌아오는 마지막점이 nr,nc가 되버려서 처음에 이것때문에 안돌아간거 같아요


    while True:
        if arr[r][c] == 3:
            return answer

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and arr[nr][nc] != 1:
                stack.append((nr, nc))
                visited[nr][nc] = 1
                r, c = nr, nc
                break
        else:
            if stack:
                r, c = stack.pop()
            else:
                answer = 0
                return answer


for test_case in range(1, 1 + T):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]

    result = maze(arr, n)
    print(f'#{test_case} {result}')
