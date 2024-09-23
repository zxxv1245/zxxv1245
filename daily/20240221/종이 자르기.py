x = [0]
y = [0]

R,C = map(int,input().split())
N = int(input())

for _ in range(N) :
    m,a = map(int,input().split())
    if m == 0 :
        y.append(a)
    elif m == 1 :
        x.append(a)

x.append(R)
y.append(C)
xl = len(x)
yl = len(y)
x.sort()
y.sort()
maxV = -21e8
for i in range(xl-1) :
    for j in range(yl-1) :
        ax = x[i]-x[i+1]
        ay = y[j]-y[j+1]
        avg = ax*ay
        if maxV < avg :
            maxV = avg

print(maxV)