# 삽입 정렬(Insertion sort)

def find_ins_idx(r: list[int], v: int):

    # result의 어느 위치에 들어가면 적당할지 찾기
    for i in range(0, len(r)):

        if(v < r[i]):
            return i

    return len(r)


def ins_sort(a: list[int]):
    result = []

    while a:
        value = a.pop(0)
        print(f"맨 앞의 원소 하나를 꺼냄 : {value}")
        print(f"현재 배열 : {a}")

        ins_idx = find_ins_idx(result, value)
        print(f"ins_idx : {ins_idx}")

        result.insert(ins_idx, value)

    return result


d = [2, 4, 5, 1, 3]
print(ins_sort(d))
