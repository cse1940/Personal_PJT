ls = []
n = int(input("숫자를 입력해 주세요. : "))
k = int(input("몇 번째 약수를 알고 싶나요? : "))

for i in range(1, n):
    if n % i == 0:
        ls.append(i)
if k > len(ls):
    print("입력한 숫자만큼의 약수가 존재하지 않습니다.")
else:
    print(f"{n}의 {k}번째 약수는 {ls[k-1]}입니다.")
