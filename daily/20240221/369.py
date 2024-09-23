N = int(input())

lst = list(map(str, range(1,N+1)))


for a in range(N) :
    cl = ''
    for b in lst[a] :
        if b in ['3','6','9'] :
            cl += '-'
            lst[a] = cl

print(*lst)