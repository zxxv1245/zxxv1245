from collections import deque

def bfs(sx,sy) :
    global flag

    Q = deque()
    Q.append((sx,sy,-1))
    visited = [0] * (n+1)
    while Q :
        ax,ay,j = Q.popleft()

        for x,y,i in lst :
            if (abs((x-ax)) + abs((y-ay))) <=1000 and i != j :
                if visited[i] > (abs((x-ax)) + abs((y-ay))) or visited[i] == 0 :
                    visited[i] = (abs((x-ax)) + abs((y-ay)))
                    Q.append((x,y,i))

    if visited[n] != 0 :
        flag = 1


t = int(input())

for Test in range(t) :
    n = int(input())
    sx,sy = map(int,input().split())
    lst = []
    for i in range(n+1) :
        x,y = map(int,input().split())
        lst.append((x,y,i))

    flag = 0
    bfs(sx,sy)

    if flag == 0 :
        print('sad')
    else :
        print('happy')