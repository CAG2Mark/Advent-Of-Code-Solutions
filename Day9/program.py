cnt = 0
nums = list()

def check_sum(num:int):
    ls = nums[-26:-1]
    print(ls)
    for i in range(24):
        for j in range(i + 1, 25):
            if num == ls[i] + ls[j]:
                return True
    return False

while True:
    try:
        num = int(input())
        nums.append(num)

        cnt += 1
        if cnt < 26: continue

        if not check_sum(num):
            print(num)
            break

    except EOFError:
        break