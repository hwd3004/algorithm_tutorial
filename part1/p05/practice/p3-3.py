# https://shoark7.github.io/programming/algorithm/피보나치-알고리즘을-해결하는-5가지-방법

# 파이썬 함수의 동작방식을 활용한 방법을 사용

def fibo(n, __cache={0: 0, 1: 1}):
    if n in __cache:
        return __cache[n]
    
    __cache[n] = fibo(n - 1) + fibo(n - 2)
    
    return __cache[n]

print(fibo(100))