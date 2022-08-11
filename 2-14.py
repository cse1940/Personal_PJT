time = int(input("시간(초)을 입력해 주세요. : "))
print(str(time) + "초 ", end="= ")
if time >= 86400:
    temp = time // 86400
    time -= temp * 86400
    print(str(temp) + "일", end=" ")
if time >= 3600:
    temp = time // 3600
    time -= temp * 3600
    print(str(temp) + "시간", end=" ")
if time >= 60:
    temp = time // 60
    time -= temp * 60
    print(str(temp) + "분", end=" ")
if time != 0:
    print(str(time) + "초")