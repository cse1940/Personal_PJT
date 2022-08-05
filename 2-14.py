time = int(input("시간(초)을 입력해 주세요. : "))
day = time / 86400
hour = (time % 86400) / 3600
minute = (time - day - hour) / 60
second = (time - day - hour) % 60

print(f"{time}초 = {day}일 {hour}시간 {minute}분 {second}초")