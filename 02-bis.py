import copy

INPUT_FILE = '02-input.txt'

class Time:
    def __init__(self, value, path=[], depth=1):
        self.value = value
        self.path = path
        self.depth = depth

def get_clean_value(s):
    return int(s[:-1])

def compute():
    computed_list = []
    global_max_depth = 0
    global_max_path = []
    with open(INPUT_FILE, 'r') as f:
        input = f.readlines()
        for i in range(len(input)):
            value = get_clean_value(input[i])
            print(i)
            #print(f"Value: {value}")
            max_depth = 1
            max_path = [value]
            times_to_remove = []
            for time in computed_list:
                #print(f"Comparing to time: {time.value} with depth {time.depth} and path {time.path}")
                if value < time.value and max_depth <= time.depth:
                    max_depth = time.depth+1
                    max_path = time.path.copy()
                    max_path.append(value)
            computed_list.append(Time(value, max_path, max_depth))
            if max_depth > global_max_depth:
                global_max_depth = max_depth
                global_max_path = max_path
                #print(f"Max depth: {global_max_depth}, max path: {global_max_path}")
    return global_max_path

def main():
    return compute()

print(main())
