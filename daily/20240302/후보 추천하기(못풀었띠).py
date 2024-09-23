N = int(input())
arr = []

M = int(input())
lst = list(map(int,input().split()))
counting = [0]*(N+1)

for i in lst :
    if len(arr) < N :
        if i not in arr :
            arr.append(i)
            counting[i] += 1
        elif i in arr :
            counting[i] += 1
    elif len(arr) == N :
        arr.pop()


