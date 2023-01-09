import sys
input = sys.stdin.readline

n = int(input())
test_p = list(map(int, input().split()))
B, C = map(int, input().split())

num = n

for i in range(n):
    if (test_p[i]-B) > 0: # 인원 중 총감독관이 볼 수 있는 인원 제외하고도 0이상일때
        num += (test_p[i]-B) // C
        if (test_p[i]-B) % C != 0:
            num += 1
    else:
        pass
print(num)