for i in range(N):
    used[k][i] = 'Q'
    queen_used[k] = 1
    for a in range(8):
        for b in range(1, N + 1):
            nx = k + dx[a] * b
            ny = i + dy[a] * b
            if 0 <= nx < N and 0 <= ny < N and used[nx][ny] == 'Q':
                used[k][i] = 0
                queen_used[k] = 0
                return