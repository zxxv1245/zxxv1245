from collections import deque
import sys
input = sys.stdin.readline
N = int(input())

lst = deque(range(1,N+1))
if len(lst) == 1 :
    print(*lst)
else :
    while True :
        lst.popleft()
        if len(lst) == 1 :
            break
        lst.append(lst.popleft())

    print(*lst)