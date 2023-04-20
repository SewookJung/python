""" 
함수를 이용하면 수학 공식을 외우지 않고, 컴퓨터에 기록해 둘 수 있다.
삼각형의 넓이를 구하는 공식 ‘밑변 * 높이 / 2’를 함수로 정의해 보라.
그 후 이 함수를 이용해 밑변의 길이가 10이고 높이가 8인 삼각형의 넓이를 계산해 출력하라.
"""


def triangle_area_calculate(base: int, height: int) -> float:
    area = (base * height) / 2
    return area


area = triangle_area_calculate(10, 8)
print(area)
