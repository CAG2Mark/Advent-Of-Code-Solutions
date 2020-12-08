count = 0

while True:
    ln = ""
    try:

        ln = input().split(": ")
        _policy = ln[0][:-2].split("-")
        policy = (int(_policy[0]), int(_policy[1]), ln[0][-1:])

        pwd = ln[1].strip()

        if (pwd[policy[0] - 1] == policy[2]) ^ (pwd[policy[1] - 1] == policy[2]): 
            count = count + 1
        
    except EOFError:
        break

print(count)