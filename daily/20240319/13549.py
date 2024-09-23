from collections import deque

def bfs() :
    global cnt,ret
    while Q :
        x = Q.popleft()
        if x == M:
            cnt += 1
            ret = lst[x]
            continue
        for i in [x-1,x+1,x*2] :
            if 0 <= i <= 100000 and ((lst[i] == 0) or (lst[i] == lst[x]+1)):
                lst[i] = lst[x]+1
                Q.append(i)


N,M = map(int,input().split())
lst = [0]*100001
Q = deque()
Q.append(N)
cnt = 0
ret = 0
bfs()
print(ret)
print(cnt)