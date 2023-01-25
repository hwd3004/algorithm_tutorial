# 숫자 n개를 리스트로 입력받아 최소값을 구하는 프로그램

def main(arr: list[int]):
    min_value = arr[0]

    for i in range(1, len(arr)):
        if min_value > arr[i]:
            min_value = arr[i]

    return min_value


v = [17, 92, 18, 33, 58, 7, 33, 42]
print(main(v))
