lst = list(input().split())


minl = []
for i in range(4) :
    arr = ''.join(lst)
    minl.append(int(arr))
    lst.insert(0,lst.pop())
minV = min(minl)
cnt = 0

for i in range(1111,minV+1)  :
    a = str(i)
    for i in range(3) :
        if a[i] < a[i+1] :
            continue
    if '0' not in a :
        cnt += 1

print(cnt)