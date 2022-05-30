# 숫자 n개 중에서 최대값 찾기를 재귀 호출로 구하기

def find_max_indx(a:list[int]):
    
    if len(a) <= 1:
        return a[0]
    
    if a[0] <= a[1]:
        a.pop(0)
    else:
        a.pop(1)
    
    # print(a)
    return find_max_indx(a)
    

v = [17, 92, 18, 33, 58, 7, 33, 42]

print(find_max_indx(v))