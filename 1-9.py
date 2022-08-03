number = int(input("정수를 입력하세요. : "))

def getSum(num):
    count = 0
    for i in range(num + 1):
        count += i
    return count
sum = getSum(number)
print(f"0부터 {number}까지의 합계는 {sum}입니다.")