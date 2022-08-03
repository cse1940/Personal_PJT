birth = int(input("생년월일을 입력해 주세요. : "))
year = birth // 10000
month = (birth % 10000) // 100
day = (birth % 10000) % 100

print(f"{year}년 {month}월 {day}일 생이네요!")