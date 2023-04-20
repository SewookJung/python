"""
다음 프로그램에서 사용된 전역변수와 지역변수를 각각 나열해 보라.
각 지역변수가 어느 함수에 속하는지도 구분해 보자.
"""


pi = 3.141592653589793


def area_of_circle(radius):
    """원의 반지름(radius)을 입력받아 넓이를 반환한다."""
    area = radius * radius * pi
    return area


def volume_of_cylinder(radius, height):
    """원기둥의 반지름(radius)과 높이(height)를 입력받아
    부피를 반환한다."""
    top_area = area_of_circle(radius)
    volume = top_area * height
    return volume


result = volume_of_cylinder(5, 10)
print(result)

# 전역변수: pi, result, area_of_circle, volume_of_cylinder, print
# 지역변수: area, top_area, volume