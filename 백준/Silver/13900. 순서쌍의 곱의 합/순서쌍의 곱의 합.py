import sys
input = sys.stdin.readline

N = int(input()) # 입력받을 정수의 개수
num_list = list(map(int, input().split())) # N개의 정수를 부여받음
total_sum = sum(num_list) # num_list의 합을 미리 계산하여 저장

ans = 0
for num in num_list:
    total_sum -= num
    ans += num * total_sum

print(ans)