
def check() :
    while True :
        k = lst[-2]-lst[-1]
        if k >= 0 :
            lst.append(k)
        elif k < 0 :
            return



N = int(input())
maxV = -21e8
for i in range(1,N+1) :
    lst = []
    j = N - i
    lst.append(N)
    lst.append(i)
    lst.append(j)
    check()
    if maxV < len(lst) :
        maxV = len(lst)
        ret = lst

print(maxV)
print(*ret)