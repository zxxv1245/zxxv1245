lst = []
for _ in range(5) :
    w = int(input())
    if w < 40 : w = 40
    lst.append(w)
print(int(sum(lst)/5))