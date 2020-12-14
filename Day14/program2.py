mem = dict()
cur_mask = ""    

def get_addrs(val, mask):
    returns = list()

    bin_str = (['0']*len(mask)) + list(bin(val)[2:])
    floating = 0;
    for i in range(len(mask)):
        bit = mask[-i - 1]
        if bit == '1':
            bin_str[-i - 1] = '1'
        elif bit == 'X':
            bin_str[-i - 1] = 'X'
            floating += 1

    for i in range(pow(2, floating)):
        floating_bin = bin(i)[2:].rjust(floating, '0')
        p = 0

        new_bin_str = bin_str.copy()

        for i in range(len(new_bin_str)):
            if new_bin_str[i] != 'X': continue
            new_bin_str[i] = floating_bin[p]
            p += 1

        new_bin_str = ''.join(new_bin_str)
        returns.append(int(new_bin_str, 2))

    return returns
        

while True:
    try:
        ln = input()
        if ln.__contains__("mask = "):
            cur_mask = ln.replace("mask = ", "")
        else:
            ln_spl = ln.split(" = ")
            addr = int(ln_spl[0][4:-1])
            val = int(ln_spl[1])

            vals = get_addrs(addr, cur_mask)
            for i in vals:
                print(i)
                mem[i] = val

    except EOFError:
        break

print(sum(mem.values()))

