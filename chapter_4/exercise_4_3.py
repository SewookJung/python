"""
두 실수가 거의 같은지 검사하는 함수 almost_equal()을 정의하라. 
이 함수는 실수 두 개를 입력받아 두 실수의 차이(오차허용범위)가 0.0001 미만이면 True를 그렇지 않으면 False를 반환한다.
또, 할 수 있다면 함수를 호출할 때 오차허용범위를 지정하도록 정의해 보라.
"""


def almost_equal(num_a: float, num_b: float, threshold: float = 0.0001) -> bool:
    return abs(num_b - num_a) < threshold


print(almost_equal(0.0055, 0.00559))  # True
print(almost_equal(0.0055, 0.0056))  # False
print(almost_equal(0.0055, 0.0056, threshold=0.001))  # True


"""
두 실수를 뺀 값의 절대값을 구하면 두 수의 차이를 알 수 있다
함수를 호출할 때 매개변수에 인자를 선택적으로 전달하도록 하려면, 매개변수에 기본값을 정의하면 됩니다
"""
