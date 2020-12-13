input()

bus = input().split(",")
times = list()
for b in bus:
    if b == 'x': times.append(-1)
    else: times.append(int(b))

# Chinese remainder theorem
# https://crypto.stanford.edu/pbc/notes/numbertheory/crt.html

M = 1
for n in bus:
    if n == 'x': continue
    M *= int(n)

s = 0
for i in range(len(bus)):
    if bus[i] == 'x': continue
    n = int(bus[i])
    a_n = n - i
    b_n = M // n
    b__n = pow(b_n, n-2, n) # inverse mod for a prime integer: https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python

    s += a_n * b_n * b__n

print(s % M)


