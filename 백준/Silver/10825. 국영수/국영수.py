import sys
input = sys.stdin.readline

n = int(input())
scores = []

for i in range(n):
    # 이름, 국어, 영어, 수학 순으로 입력
    scores.append(input().split())
    scores[i][1] = int(scores[i][1])
    scores[i][2] = int(scores[i][2])
    scores[i][3] = int(scores[i][3])

scores.sort(key = lambda x : (-x[1], x[2], -x[3], x[0]))

for i in range(n):
    print(scores[i][0])