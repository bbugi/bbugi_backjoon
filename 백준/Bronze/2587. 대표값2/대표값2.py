nums = []
for i in range(5):
    n = int(input())
    nums.append(n)
    nums.sort()

# 평균값
print(int(sum(nums)/len(nums)))

# 중앙값
print(nums[2])