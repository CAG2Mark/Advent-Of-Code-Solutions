mem = [0]*100000
cur_mask = ""

def set_bit(val, mask):
    bin_str = (['0']*len(mask)) + list(bin(val)[2:])
    for i in range(len(mask)):
        bit = mask[-i - 1]
        if bit == 'X':
            bin_str[-i - 1] = bit

    bin_str = ''.join(bin_str)

    return int(bin_str, 2)
        

while True:
    try:
        ln = input()
        if ln.__contains__("mask = "):
            cur_mask = ln.replace("mask = ", "")
        else:
            ln_spl = ln.split(" = ")
            addr = int(ln_spl[0][4:-1])
            val = int(ln_spl[1])

            mem[addr] = set_bit(val, cur_mask)

    except EOFError:
        break

print(sum(mem))

