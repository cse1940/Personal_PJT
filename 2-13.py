def max_(num):
    temp_max = 0
    
    for i in range(1, len(num)):
        if num[i] > num[temp_max]:
            temp_max = i
    return temp_max

ls = [1999, 10, 6, 24, 25, 99999]
print(max_(ls))
