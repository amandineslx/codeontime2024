INPUT_FILE = '02-input.txt'


def get_best_progression(considered_list):
    progression_so_far = [considered_list[0]]
    best_progression = []
    remaining_values = [x for x in considered_list if x < considered_list[0]]
    #print(f"Remaining values: {remaining_values}")
    if not remaining_values:
        return progression_so_far
    for i in range(len(remaining_values)):
        #print(i)
        value = remaining_values[i]
        possible_progression = progression_so_far.copy()
        possible_progression.extend(get_best_progression(remaining_values[i:]))
        if len(possible_progression) > len(best_progression):
            #print(f"Considered {possible_progression} better than {best_progression}")
            best_progression = possible_progression
    #print(f"Best progression: {best_progression}")
    return best_progression

def compute():
    best_progression = []
    with open(INPUT_FILE, 'r') as f:
        considered_list = [int(x[:-1]) for x in f.readlines()]
        while len(considered_list) > len(best_progression):
            computed_progression = get_best_progression(considered_list)
            print("I am still here")
            if len(computed_progression) > len(best_progression):
                best_progression = computed_progression
            considered_list = considered_list[1:]
        return best_progression

def main():
    return compute()

print(main())
