# https://shoark7.github.io/programming/algorithm/피보나치-알고리즘을-해결하는-5가지-방법

# 기본 재귀적 풀이
def fibo(n):
    if n <= 1:
        return n
    
    return fibo(n-1) + fibo(n-2)

for i in range(1, 100):
    print(i, fibo(i))
    pass

