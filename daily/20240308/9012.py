T = int(input())

for Test in range(1,T+1) :
    lst = list(input())
    st = []
    ret = 0
    for i in lst :
        if i == '(' :
            st.append(i)
        elif not st and i == ')' :
            ret = 1
            break
        elif st and st[-1] == '(' and i == ')' :
            st.pop()

    if st :
        ret = 1

    if ret == 1 :
        print('NO')
    else :
        print('YES')