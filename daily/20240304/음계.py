lst = list(map(int,input().split()))

start = lst[0]
end = lst[0]
cntA = 1
cntB = 1
for i in lst[1:] :
    if start < i :
        start = i
        cntA += 1
    if end > i :
        end = i
        cntB += 1

if cntA == 8 :
    print('ascending')
elif cntB == 8 :
    print('descending')
else :
    print('mixed')