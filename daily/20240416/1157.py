word = input().upper()
dict = dict()

for a in word :
    if a in dict :
        dict[a] += 1
    else :
        dict[a] = 1

max_dict = -21e8
for i in dict :
    if max_dict < dict[i] :
        max_dict = dict[i]

lst = []
for a in dict :
    if dict[a] == max_dict :
        lst.append(a)

if len(lst) >= 2 :
    print('?')
else :
    print(lst[0])