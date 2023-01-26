# 찾는 값이 나오는 모든 위치를 리스트로 돌려주는 탐색 알고리즘
# 찾는 값이 리스트에 없다면 빈 리스트인 []를 돌려줌

def search_list(a: list[int], *x: int):

    result = []

    for i in range(0, len(a)):
        for j in range(0, len(x)):
            if a[i] == x[j]:
                result.append(i)
                break

    return result


v = [17, 92, 18, 33, 58, 7, 33, 42]
print(search_list(v, 33, 58))
