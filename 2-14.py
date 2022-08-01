time = int(input("시간(초)을 입력해 주세요. : "))
day = time // 86400
hour = -(time - 86400) // 3600
minute = (time - hour*3600) // 60
second = time - day - hour - minute
print(f"{time}초 = {day}일 {hour}시 {minute}분 {second}초")