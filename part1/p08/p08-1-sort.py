# 선택 정렬
# 주어진 리스트 안의 자료를 작은 수부터 큰 수 순서로 배열하는 정렬 알고리즘
# 자료를 크기 순서대로 맞춰 일렬로 나열

def find_min_idx(a):
    n = len(a)
    min_idx = 0
    
    for i in range(1, n):
        if a[i] < a[min_idx]:
            min_idx = i
    
    return min_idx

def sel_sort(a:list):
    result = []
    
    while a:
        min_idx = find_min_idx(a)
        value = a.pop(min_idx)
        result.append(value)
    
    return result

d = [2, 4, 5, 1, 3]
print(sel_sort(d))
