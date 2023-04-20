"""
프로그래머 세 사람이 자신의 나이를 말하고 있다.
세 사람의 출생년도를 각각 구하라.
"""


programmer_a: str = "저는 0x7d0년에 태어났습니다. 올해로 0x12살이 되었네요."
programmer_b: str = "그러시군요. 저는 올해 0o22세입니다."
programmer_c: str = "저는 18살입니다."

"""
Convert hexadecimal to decimal
---
0x7d0
0 * 1 = 0
d(13) * 16 = 208
7 * 16 * 16 = 1792
0 + 208 + 1792 = 2000

Convert octal decimal to decimal
---
0o22
2 * 8 ** 0 = 2
2 * 8 ** 1 = 16
2 + 16 = 18
"""

# 세명 모두 2000년 생이다.
