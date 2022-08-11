a, b = map(int, input("숫자 두 개를 입력해 주세요.(예: 3 5) : ").split(" "))
c = int(input("배수를 알고 싶은 숫자를 입력해 주세요. : "))

for i in range(a, b + 1):
    if i % c == 0:
        print(i, end=" ")
    