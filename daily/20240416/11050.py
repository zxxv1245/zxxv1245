from itertools import combinations

N,K = map(int,input().split())
lst = [i for i in range(1,N+1)]
ret = list(combinations(lst,K))
print(len(ret))