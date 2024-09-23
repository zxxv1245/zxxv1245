def abc(k) :
    global cnt

    if k == 10 :
        cnt += 1
        return

    for i in range(10) :
        if visited[i] == 0 :
            visited[i] = 1
            path[k] = i
            abc(k+1)
            visited[i] = 0


visited = [0]*10
path = [0]*10
cnt = 0
abc(0)
print(cnt)