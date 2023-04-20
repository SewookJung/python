"""
네 개의 수를 매개변수로 입력받아 평균을 계산해 반환하는 함수
average_of_4_numbers()를 정의하라.
이 함수를 이용해 512, 64, 256, 192의 평균을 계산하고 화면에 출력하라.
"""


def average_of_4_numbers(num_a: int, num_b: int, num_c: int, num_d: int) -> float:
    average = (num_a + num_b + num_c + num_d) / 4
    return average


average_of_4_numbers(512, 64, 256, 192)
