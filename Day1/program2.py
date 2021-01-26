# Pythonista and working copy test

nums = list()

while True:
    try:
        nums.append(int(input()))
    except EOFError:
        break

sum = 0

nums.sort()

# O(n^3) 
for i in range(len(nums)):
    for j in range(i, len(nums)):
        for k in range(j, len(nums)):
            sum = nums[i] + nums[j] + nums[k]
            if sum == 2020:
                print(nums[i] * nums[j] * nums[k])
