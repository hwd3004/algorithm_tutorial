# 1.
# 1부터 n까지의 합 구하기를 재귀 호출로 만들기

def sum_n(n: int):
    if n == 1:
        return 1

    return n + sum_n(n-1)


print(sum_n(10))

# 2.
# 숫자 n개 중에서 최대값 찾기를 재귀 호출로 만들기


def max_n(a: list[int]):
    if len(a) == 1:
        return a[0]

    if a[0] < a[1]:
        a.pop(0)
        return max_n(a)
    else:
        a.pop(1)
        return max_n(a)


v = [17, 92, 18, 33, 58, 7, 33, 42]
print(max_n(v))

# 2-2.


def find_max(a: list[int], n: int):  # 리스트 a의 앞부분 n개 중 최대값을 구하는 재귀 함수
    if n == 1:
        return a[0]

    max_n_1 = find_max(a, n - 1)  # n - 1개 중 최대값을 구함

    if max_n_1 > a[n - 1]:  # n - 1개 중 최대값과 n - 1번 위치 값을 비교
        return max_n_1
    else:
        return a[n - 1]


v = [17, 92, 18, 33, 58, 7, 33, 42]
print(find_max(v, len(v)))
