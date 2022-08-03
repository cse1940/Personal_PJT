def multiplication(x):
    for i in range(1, 10):
        print(f"{x} * {i} = {x*i}")


while True:
    number = int(input("2~9 사이의 숫자를 입력해 주세요. (1을 누르면 프로그램이 종료됩니다.) "))
    if number == 1:
        print("프로그램이 종료합니다.")
        break
    elif 2 <= number <= 9:
        multiplication(number)
    else:
        print("범위 외의 숫자입니다. 다시 시도하세요.")