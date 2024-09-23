import copy
import sys
input = sys.stdin.readline

                                                                                                                                   
K, N = map(int, input().split())
lst = []
for _ in range(K):
    lan = int(input())
    lst.append(lan)

ret = 1
while True:
    arr = copy.deepcopy(lst)
    cnt = 0
    a = 0
     
