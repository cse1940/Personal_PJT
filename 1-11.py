ls = []
for i in range(7):
    number = int(input("정수를 입력하세요. : "))
    ls.append(number)

count = 0
for l in ls:
    count += l
print(f"평균 : {count / 7}")