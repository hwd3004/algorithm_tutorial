# https://shoark7.github.io/programming/algorithm/피보나치-알고리즘을-해결하는-5가지-방법

# 재귀적 동적 계획법 풀이

def fibo(n):
    cache = [1 for _ in range(n + 1)]
    
    def iterate(n):
        # 기저 사례 1.
        if n <= 1:
            return n
    
        # 기저 사례 2.
        if cache[n] != 1:
            return cache[n]
        
        # 기저 사례 충족 못할 시 값을 실제로 구함
        cache[n] = iterate(n - 1) + iterate(n - 2)
        
        return cache[n]
    
    return iterate(n)

for n in range(1, 12):
    print(n, fibo(n))
    pass