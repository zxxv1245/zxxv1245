def bfs() :

    while Q :
        x = Q.popleft()

        if x == K :
            print(lst[x])
            return
        for i in [x-1,x+1] :
            if 0<= i <= 100000 and i not in ret :
                lst[i] = lst[x] + 1
                Q.append(i)
                ret.append(i)
        j = x*2
        if 0<= j <= 100000 and j not in ret :
            lst[i] = lst[x]
            Q.append(j)
            ret.append(j)

from collections import deque
import sys
input = sys.stdin.readline

N,K = map(int,input().split())

lst = [0]*100001
Q = deque()
Q.append(N)
ret = []
ret.append()

bfs()


