# def getwinner(left, right):
#     if lst[left] == 1 and lst[right] == 2:
#         return right
#     elif lst[left] == 2 and lst[right] == 3:
#         return right
#     elif lst[left] == 3 and lst[right] == 1:
#         return right
#     elif lst[left] == 2 and lst[right] == 1:
#         return left
#     elif lst[left] == 3 and lst[right] == 2:
#         return left
#     elif lst[left] == 1 and lst[right] == 3:
#         return left
#     else:
#         return left


def game(i, j):
    if i == j:
        return i
    else :
        left = game(i, (i + j) // 2)
        right = game((i + j) // 2 + 1, j)

        if lst[left] == 1 and lst[right] == 2:
            return right
        elif lst[left] == 2 and lst[right] == 3:
            return right
        elif lst[left] == 3 and lst[right] == 1:
            return right
        elif lst[left] == 2 and lst[right] == 1:
            return left
        elif lst[left] == 3 and lst[right] == 2:
            return left
        elif lst[left] == 1 and lst[right] == 3:
            return left
        else:
            return left




T = int(input())

for Test in range(1, T + 1):
    N = int(input())
    lst = [0] + list(map(int, input().split()))

    print(f'#{Test} {game(1, N)}')