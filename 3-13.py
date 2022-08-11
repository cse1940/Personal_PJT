a, b = map(int, (input("24시 기준의 시간을 입력해 주세요. : ").split(":")))

if 12 < a < 24:
    print(f"변환 시간: {a - 12}:{b} PM")
elif a < 12:
    print(f"변환 시간: {a}:{b} AM")
elif a < 0 or a > 24:
    print("잘못 입력하였습니다. 다시 입력해 주세요.")
else:
    print(f"변환 시간: {a}:{b} PM")