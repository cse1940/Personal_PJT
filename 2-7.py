def circle(x):
    return x * x * 3.14

def triangle(x, y):
    return x * y / 2

def rectangle(x, y):
    return x * y

def square(x):
    return x * x

print("""
=======도형 목록=======
1. 원
2. 삼각혐
3. 직사각형
4. 정사각형
=======================
""")

number = int(input("도형 목록에서 넓이를 계산할 도형의 번호를 입력해 주세요. : "))

if number == 1:
    a = int(input("원의 반지름 길이를 입력해 주세요. : "))
    print(f"반지름이 {a}인 원의 넓이는 약 {circle(a)}입니다.")
elif number == 2:
    a = int(input("삼각형의 밑변의 길이를 입력해 주세요. : "))
    b = int(input("삼각형의 높이의 길이를 입력해 주세요. : "))
    print(f"밑변이 {a}이고 높이가 {b}인 삼각형의 넓이는 {triangle(a, b)}입니다.")
elif number == 3:
    a = int(input("직사각형의 가로의 길이를 입력해 주세요. : "))
    b = int(input("직사각형의 세로의 길이를 입력해 주세요. : "))
    print(f"가로가 {a}이고 세로가 {b}인 직사각형의 넓이는 {rectangle(a,b)}입니다.")
elif number == 4:
    a = int(input("정사각형의 한 변의 길이를 입력해 주세요. : "))
    print(f"한 변이 {a}인 정사각형의 넓이는 {square(a)}입니다.")
else:
    print("다시 입력해 주세요.")

