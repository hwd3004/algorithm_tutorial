# Exchange Sort

def exchange(S: list[int]):
    n = len(S)

    for i in range(n-1):
        for j in range(i + 1, n):
            if(S[i] > S[j]):

                S[i], S[j] = S[j], S[i]
                # 파이썬에서 스왑하는 코드
                # 다른 언어에서 temp = x, x = y, y y = temp 로 하는 것
                # 파이썬에선 내부적으로 (S[j], S[i]) 튜플을 만들어서 (S[i], S[j]) 튜플에 저장하는 내부적인 구현이 있음
            print(S)
        
        # print(S)

    return S


S = [10, -1, 7, 11, 5, 13, 8]
res = exchange(S)
print(res)
