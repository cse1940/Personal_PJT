ls = []

word = input("단어를 입력해 주세요. : ")

for i in word:
    ls.append(i)

a = ls[::-1]
if ls == a:
    print(f"{word}는 회문입니다.")
else:
    print("회문이 아닙니다.")