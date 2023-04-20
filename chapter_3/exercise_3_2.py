def print_absolute():
    """정수를 입력받아 절대값을 출력하는 함수"""
    print("정수를 입력하세요.")
    number = int(input())
    print(f"{number}의 절대값:", abs(number))


print_absolute()
