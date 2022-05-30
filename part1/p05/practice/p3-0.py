# https://shoark7.github.io/programming/algorithm/피보나치-알고리즘을-해결하는-5가지-방법

# 반복적 동적 계획법 풀이

cache = [0 for _ in range(100+1)]
cache[1] = 1

for i in range(2, 100+1):
    cache[i] = cache[i-1] + cache[i-2]

print(cache[100])