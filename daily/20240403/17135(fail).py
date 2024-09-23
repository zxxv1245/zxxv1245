from itertools import combinations
import copy
N,M,D = map(int,input().split())

lst = [list(map(int,input().split())) for _ in range(N)]

arr = []
for a in range(M) :
    arr.append((N,a))

combi = combinations(arr,3)
