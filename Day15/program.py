mem = dict()

def search(num, cur):
    if not num in mem.keys(): return 0
    return max(0, cur - mem[num])

ln = input().split(",")
nums = [int(x) for x in ln] + [-1] * (2020 - len(ln))

for i in range(len(nums)):
    print(i)
    if nums[i] == -1: 
        nums[i] = search(nums[i-1], i-1)

    if i != 0:
        mem[nums[i-1]] = i-1

print(nums[2019])