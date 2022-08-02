score1 = int(input("국어 점수를 입력하세요. : "))
score2 = int(input("수학 점수를 입력하세요. : "))
score3 = int(input("영어 점수를 입력하세요. : "))
score4 = (score1 + score2 + score3) / 3

if score4 >= 50:
    print(f"평균 점수는 {score4}점으로 합격입니다.")
else:
    print(f"평균 점수는 {score4}점으로 불합격입니다.")