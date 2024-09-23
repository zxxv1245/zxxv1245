for _ in range(4) :
    si1,sj1,ei1,ej1,si2,sj2,ei2,ej2 = map(int,input().split())

    if ei1 < si2 or ej1 < sj2 or ei2 < si1 or ej2 < sj1 :
        print('d')
    elif sj2 == ej1 or sj1 == ej2 :
        if si2 == ei1 or si1 == ei2 :
            print('c')
        else :
            print('b')

    elif si2 == ei1 or si1 == ei2 :
        if sj2 == ej1 or sj1 == ej2 :
            print('c')
        else :
            print('b')

    else :
        print('a')