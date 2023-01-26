# 재귀호출을 이용한 시에르핀스키(Sierpinski) 삼각형 그리기

import turtle as t


def tri(tri_len: int):
    if tri_len <= 10:  # 길이가 10 이하이면 종료.
        for i in range(0, 3):  # 각 변의 길이를 각각 10으로 설정 후 삼각형을 그린다.
            t.forward(tri_len)  # 삼각형의 변을 그린다.
            t.left(120)  # 삼각형의 변을 그린다.

        return

    new_len = tri_len / 2  # 재귀호출을 이용한 시에르핀스키(Sierpinski) 삼각형 그리기
    tri(new_len)  # 왼쪽 삼각형을 그리기
    t.forward(new_len)
    tri(new_len)  # 오른쪽 삼각형을 그리기
    t.backward(new_len)
    t.left(60)
    t.forward(new_len)
    t.right(60)
    tri(new_len)
    t.left(60)
    t.backward(new_len)
    t.right(60)


t.speed(0)
tri(160)
t.hideturtle()
t.done()
