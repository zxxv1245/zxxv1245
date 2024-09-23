from collections import deque
import sys
input = sys.stdin.readline
def bfs(start,end) :

    Q = deque()
    Q.append((start,''))
    visited = [0]*10000

    while Q :
        v, result = Q.popleft()
        if v == end :
            return result
        for a in ['L','R','S','D'] :
            if a == 'L' :
                L = v//1000
                new_v = (v*10 + L)%10000
                if visited[new_v] == 0 :
                    Q.append((new_v,result+'L'))
                    visited[new_v] = 1
            elif a == 'R' :
                R = v % 10
                new_v = v//10 + R*1000
                if visited[new_v] == 0 :
                    Q.append((new_v, result + 'R'))
                    visited[new_v] = 1
            elif a == 'S' :
                new_v = (v+9999)%10000
                if visited[new_v] == 0 :
                    Q.append((new_v, result + 'S'))
                    visited[new_v] = 1
            elif a == 'D' :
                new_v = (v * 2)%10000
                if visited[new_v] == 0 :
                    Q.append((new_v,result+'D'))
                    visited[new_v] = 1
T = int(input())
for _ in range(T) :
    start, end = map(int,input().split())

    print(bfs(start,end))
