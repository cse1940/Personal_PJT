n = int(input("숫자를 입력해 주세요. : "))

num = 2
while num <= n:
    if n % num == 0:
        print(num, end=" ")
        n /= num
    else:
        num += 1