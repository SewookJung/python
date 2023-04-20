"""
사용자로부터 두 개의 텍스트를 입력받아, 입력받은 내용을 출력하는 프로그램을 작성해 보라.
예를 들어 사용자가 카페라테, 쿠키라고 입력 한다면 실행 결과는 다음과 같다.
"""

"""
Example
---
주문하실 음료: 카페라테
주문하실 간식: 쿠키
카페라테 쿠키 주문 받았습니다.
"""

drink = input("주문하실 음료: ")
dessert = input("주문하실 간식: ")
print(f"{drink} {dessert} 주문 받았습니다.")


# 답

print("주문하실 음료: ", end="")
ordered_drink = input()

print("주문하실 간식: ", end="")
ordered_dessert = input()

print(ordered_drink, ordered_dessert, "주문 받았습니다.")