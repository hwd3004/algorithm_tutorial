# Bubble Sort

def bubble_sort(a: list[int]):

    n = len(a)

    isSorted = False

    for i in range(0, n - 1):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
            isSorted = True

    if isSorted:
        bubble_sort(a)
    else:
        return a


d = [2, 4, 5, 1, 3]
bubble_sort(d)
print(d)
