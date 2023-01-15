num_list = [i for i in range(1,10001)]

for i in range(1, 10001):
    num = i + (i // 1000) + (i // 100)%10 + (i // 10)%10 + (i % 10)
    if num in num_list:
        num_list.remove(num)

for i in range(len(num_list)):
    print(num_list[i])