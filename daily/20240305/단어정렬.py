N = int(input())
lst = []
for _ in range(N):
    w = input()
    if w not in lst:
        lst.append(w)

lst.sort()
lst.sort(key=lambda x: len(x))

for i in lst:
    print(i)
