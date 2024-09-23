from collections import deque

N,K = map(int,input().split())

Q = deque(range(1,N+1))
print('<', end = '')
while Q :
    for i in range(K-1) :
        Q.append(Q.popleft())
    if len(Q) != 1 :
        print(f'{Q.popleft()}, ',end= '')
    else :
        print(f'{Q.popleft()}',end='')
print('>')

