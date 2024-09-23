from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
Q = deque()

for _ in range(N) :
    arr = input().strip().split()

    if arr[0] == 'push_back' : Q.append(arr[1])
    if arr[0] == 'push_front' : Q.insert(0,arr[1])
    elif arr[0] == 'pop_front' :
        if Q : print(Q.popleft())
        else : print(-1)
    elif arr[0] == 'pop_back' :
        if Q : print(Q.pop())
        else : print(-1)
    elif arr[0] == 'size' : print(len(Q))
    elif arr[0] == 'empty' :
        if Q : print(0)
        else : print(1)
    elif arr[0] == 'front' :
        if Q : print(Q[0])
        else : print(-1)
    elif arr[0] == 'back' :
        if Q : print(Q[-1])
        else : print(-1)


