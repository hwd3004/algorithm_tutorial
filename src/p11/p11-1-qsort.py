# 퀵 정렬

def quick_sort(a: list[int]):
    n = len(a)

    if n <= 1:
        return a

    pivot = a[-1]  # 편의상 리스트의 마지막 값을 기준 값으로 정함
    print("pivot", pivot)

    g1, g2 = [], []

    for i in range(0, n - 1):
        if a[i] < pivot:
            g1.append(a[i])
            print("g1", g1)
        else:
            g2.append(a[i])
            print("g2", g2)

    return quick_sort(g1) + [pivot] + quick_sort(g2)


d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
print(quick_sort(d))
