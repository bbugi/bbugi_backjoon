import sys
input = sys.stdin.readline

n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))
for i in sorted(nums): # num.sort() 말고 다른 방식으로 정렬해봄!
    print(i)