N = int(input())
lst = list(map(int,input().split()))
M = int(input())
arr = list(map(int,input().split()))
result = {}
for a in arr :
    result[a] = 0

for b in lst :
    try :
        result[b] += 1
    except :
        pass
for c in arr:
    print(result[c], end = ' ')