import sys
input = sys.stdin.readline

score = []

for i in range(5):
    num = int(input())
    if num < 40 :
        num = 40
    score.append(num)

# print(score)

ans = sum(score) / 5

print(int(ans))