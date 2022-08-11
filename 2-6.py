answer = input("퀴즈 결과를 입력해 주세요.(예: OOXOXXO): ").split("X")
score = 0

for i in answer:
    for j in range(0, len(i) + 1):
        score += j
print(score)


