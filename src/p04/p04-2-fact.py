# 연속한 숫자의 곱을 구하는 알고리즘
# 입력: n
# 출력: 1부터 n까지 연속한 숫자를 곱한 값

# 1! = 1
#
# 2! = 2 × 1 = 2 × 1!
#
# 3! = 3 × (2 × 1) = 3 × 2!
#
# 4! = 4 × (3 × 2 × 1) = 4 × 3!
#
# n! = n × (n -1)!

def fact(n: int):
    if n <= 1:
        return 1

    return n * fact(n - 1)


print(fact(5))
print(fact(10))
