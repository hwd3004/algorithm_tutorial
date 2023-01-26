# 선택 정렬

def sel_sort(a: list[int]):
    n = len(a)

    for i in range(0, n - 1):
        min_inx = i

        for j in range(i + 1, n):
            if a[j] < a[min_inx]:
                min_inx = j

        a[i], a[min_inx] = a[min_inx], a[i]


d = [2, 4, 5, 1, 3]
sel_sort(d)
print(d)
