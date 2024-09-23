A,B = map(int,input().split())
Alst = []
Blst = []
for a in range(1,A//2+1) :
    if A % a == 0 :
        Alst.append(a)
        Alst.append(int(A/a))
Alst.sort()

for a in range(1,B//2+1) :
    if B % a == 0 :
        Blst.append(a)
        Blst.append(int(B/a))

print(Alst)
print(Blst)
ret1 = 1
for a in reversed(Alst) :
    if a in Blst :
        ret1 = a
        break

AB = A*B/ret1
ret2 = AB

print(ret1)
print(int(ret2))