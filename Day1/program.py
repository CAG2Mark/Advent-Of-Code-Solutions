nums = list()

while True:
    try:
        nums.append(int(input()))
    except EOFError:
        break

sum = 0

nums.sort()

i = 0
j = len(nums) - 1
# O(n logn) 
while sum != 2020:
    sum = nums[i] + nums[j]
    if sum > 2020: j = j - 1
    if sum < 2020: i = i + 1

print(nums[i] * nums[j])