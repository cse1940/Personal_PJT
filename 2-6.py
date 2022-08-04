answer = input("퀴즈 결과를 입력해 주세요.(예: OOXOXXO): ").split("X")
score = 0
count = 0

for i in answer:
    count += 1
    score += count
print(score)


