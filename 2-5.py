number = int(input("숫자를 입력해 주세요. : "))
count = 1

for i in range(1, number + 1):
    count *= i
print(f"{number}!은 {count}입니다.")
