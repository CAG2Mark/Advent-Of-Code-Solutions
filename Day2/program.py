count = 0

while True:
    ln = ""
    try:

        ln = input().split(": ")
        _policy = ln[0][:-2].split("-")
        policy = (int(_policy[0]), int(_policy[1]), ln[0][-1:])

        sum = 0
        for ch in ln[1].strip():
            if ch == policy[2]: sum = sum + 1

        if sum <= policy[1] and sum >= policy[0]: count = count + 1
        
    except EOFError:
        break

print(count)