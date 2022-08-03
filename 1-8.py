count = 0

for i in range(2, 101, 2):
    if i % 7 != 0:
        count += 1
print(f"짝수이면서 7의 배수가 아닌 수의 갯수는 {count}")