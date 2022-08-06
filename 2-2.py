sen = input("문장을 입력해 주세요. : ").split(" ")
sen_ = list(set(sen))
sen_.sort()
for i in sen_:
    print(i, end=" ")
