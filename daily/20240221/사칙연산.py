def abc(root) :   # 후위순회 => LRV(왼쪽,오른쪽,자기자신)
    if root == 0 : # 기저조건
        return

    abc(leftC[root]) # L
    abc(rightC[root]) # R
    # V



for Test in range(1,11) :
    N = int(input()) # 갯수

    leftC = [0]*(N+1) # 왼쪽 자식 노드 저장할 list
    rightC = [0]*(N+1) # 오른쪽 자식 노드 저장할 list
    lst = [0]*(N+1) # 값을 저장할 list

    for _ in range(N) :
        s = input().split()   # 노드번호, 연산자 or 피연산자, 왼쪽 자식, 오른쪽 자식 (문자열 주의)

        if len(s) == 4 :   # 입력 형태 ex) 1 - 2 3 과 같은 형태
            lst[int(s[0])] = s[1] # 연산자
            leftC[int(s[0])] = int(s[2])
            rightC[int(s[0])] = int(s[3])
        elif len(s) == 2 : # 입력 형태 ex) 3 10 과 같은 형태
            lst[int(s[0])] = int(s[1]) # 자식 노드가 없을땐 값이 연산자가 아닌 피연산자이기 때문에 int로 변환

    abc(1)
    print(f'#{Test} {lst[1]}')  # 다시 풀어보기....