import sys

input = sys.stdin.readline

n = int(input())
dis_sati = 0
pred_rank = []

for i in range(n):
    pred_rank.append(int(input()))

# pred_rank.sort()
pred_rank = sorted(pred_rank)

for idx, rank in enumerate(pred_rank):
    dis_sati += abs(rank - (idx+1))
print(dis_sati)
