N = int(input())

lst = [list(map(int,input().split())) for _ in range(N)]


start = lst[0][0]
end = lst[0][1]
ret = 0
for x,y in lst[1:] :

    if end >= x and end < y:
        end = y
    elif end >= x and end > y :
        continue
    elif end < x :
        ret += (end-start)
        start = x
        end = y

result = ret + (end-start)
print(result)