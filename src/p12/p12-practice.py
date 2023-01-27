# 다음 과정을 참고하여 재귀 호출을 사용한 이분 탐색 알고리즘을 만들어 보기
# ① 주어진 탐색 대상이 비어 있다면 탐색할 필요가 없습니다(종료 조건).
# ② 찾는 값과 주어진 탐색 대상의 중간 위치 값을 비교합니다.
# ③ 찾는 값과 중간 위치 값이 같다면 결괏값으로 중간 위치 값을 돌려줍니다.
# ④ 찾는 값이 중간 위치 값보다 크다면 중간 위치의 오른쪽을 대상으로 이분 탐색 함수를 재귀 호출합니다.
# ⑤ 찾는 값이 중간 위치 값보다 작다면 중간 위치의 왼쪽을 대상으로 이분 탐색 함수를 재귀 호출합니다.

def binary_search(data: list[int], target: int, start=None, end=None):
    if len(data) == 0:
        return False

    mid = len(data) // 2

    if start != None and end != None:
        mid = (start + end) // 2

    if data[mid] == target:
        return mid

    if data[mid] < target:
        return binary_search(data, target, mid + 1, len(data) - 1)
    else:
        return binary_search(data, target, 0, mid - 1)


d = [1, 4, 9, 16, 25, 36, 49, 64, 81]
print(binary_search(d, 36))
