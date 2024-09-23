for Test in range(1,11) :
    N = int(input()) # 입력
    # 정점의 갯수 만큼  정점의 정보를 받는다.
    leftC = [0]*(N+1) # 왼쪽 자식 정점 정보 받는 배열
    rightC = [0]*(N+1) # 오른쪽 자식 정점 정보 받는 배열
    lst = [0]*(N+1) # 정점 데이터를 저장하는 배열
    # 트리의 정보를 기록할 수 있는 공간 생성
    for _ in range(N) :
        s = input().split()

        if len(s) == 4 :
            lst[int(s[0])] = s[1]
            leftC[int(s[0])] = int(s[2])
            rightC[int(s[0])] = int(s[3])
        elif len(s) == 2 :
            lst[int(s[0])] = int(s[1])

    # 로직(수식 트리 -> 후위표현식)
    # 후위표현식 -> 결과값 출력
    # 후위순회가 진행 되는 코드
    # 출력
    def post_order(v) :
        if v == 0 :
            return
        post_order(leftC[v]) # L
        post_order(rightC[v]) # R
        # V 후위순회
        # 현재 노드가 연산자이다면... 왼쪽 자식의 값과 오른쪽 자식의 값 가지고 연산
        if lst[v] == '+' :
            lst[v] == lst[leftC[v]] + lst[rightC[v]] # L + R
        elif lst[v] == '-' :
            lst[v] == lst[leftC[v]] - lst[rightC[v]] # L - R
        elif lst[v] == '*' :
            lst[v] == lst[leftC[v]] * lst[rightC[v]] # L * R
        elif lst[v] == '/' :
            lst[v] == lst[leftC[v]] // lst[rightC[v]] # L // R


    post_order(1)