# 왼쪽으로 별 정렬
n = int(input("삼각형의 높이를 입력해 주세요. : "))
for i in range(1, n + 1):
    print("*" * i)

# 오른쪽으로 별 정렬
n = int(input("삼각형의 높이를 입력해 주세요. : "))
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i )
