import sys

nums = sys.stdin.readline().split()

for i in range(len(nums)):
    nums[i] = int(nums[i])**2

print(sum(nums) % 10)