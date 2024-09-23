import sys
input = sys.stdin.readline

arr = [1] * 1000001
arr[0] = arr[1] = 0
for i in range(2,1001):
    if arr[i] == 1:
        for j in range(i+i,1000001,i):
            arr[j] = 0
while True :
    N = int(input())
    if N == 0 :
        break



    for i in range(3,N+1,2) :
        if arr[i] and arr[N-i]:
            print(f'{N} = {i} + {N-i}')
            break

