cnt = 0
nums = list()

invalid = 0

def check_sum(num:int):
    ls = nums[-26:-1]
    for i in range(24):
        for j in range(i + 1, 25):
            if num == ls[i] + ls[j]:
                return True
    return False

def find_sum_len(len):
    global cnt, invalid
    for i in range(cnt - len + 1):
        if sum(nums[i:i + len]) == invalid:
            return max(nums[i:i + len]) + min(nums[i:i + len])
    return 0

while True:
    try:
        num = int(input())
        nums.append(num)

        cnt += 1
        if cnt < 26: continue
        if not check_sum(num):
            invalid = num
            break

    except EOFError:
        break

print("Invaid number is " + str(invalid))

for i in range(2, cnt):
    val = find_sum_len(i)
    if val:
        print(val)