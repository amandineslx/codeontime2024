INPUT_FILE = '03-input.txt'

def read_input():
    ins = []
    outs = []
    with open(INPUT_FILE, 'r') as f:
        for line in f.readlines():
            number,enter,out = line[:-1].split(",")
            ins.append(int(enter))
            outs.append(int(out))
    ins.sort()
    outs.sort()
    return ins, outs

def compute():
    ins,outs = read_input()
    in_it = 0
    out_it = 0
    instantaneous = 0
    max = 0
    while in_it < len(ins) and out_it < len(outs):
        if ins[in_it] < outs[out_it]:
            print(f"{ins[in_it]} smaller than {outs[out_it]}")
            in_it = in_it+1
            instantaneous = instantaneous+1
            if instantaneous > max:
                max = instantaneous
        elif ins[in_it] > outs[out_it]:
            print(f"{ins[in_it]} greater than {outs[out_it]}")
            out_it = out_it+1
            instantaneous = instantaneous-1
        else:
            print(f"{ins[in_it]} equals {outs[out_it]}")
            in_it = in_it+1
            out_it = out_it+1
    return max

def main():
    return compute()

print(main())
