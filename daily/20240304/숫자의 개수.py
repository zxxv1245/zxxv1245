
ret = 1
for i in range(3) :
    ret *= int(input())

lst = [0]*10

for j in str(ret) :
    lst[int(j)] += 1

for k in lst :
    print(k)
