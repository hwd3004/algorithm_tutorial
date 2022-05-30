# https://shoark7.github.io/programming/algorithm/피보나치-알고리즘을-해결하는-5가지-방법

# 반복적 풀이

def fibo(n):
    if n <= 1:
        return n
    
    a, b = 0, 1
    
    for i in range(n-1):
        a, b = b, a + b
        
    return b

for n in range(1, 100):
    print(n, fibo(n))