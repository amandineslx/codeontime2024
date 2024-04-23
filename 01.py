INPUT_FILE = '01-input.txt'

def compute_best_contry():
    countries = dict()
    minimal_time = -1
    with open(INPUT_FILE, 'r') as f:
        for result in f.readlines():
            _, country, time_s = result.split(",")
            if country not in countries:
                countries[country] = 0
            countries[country] = countries[country] + int(time_s)
    return min(countries, key=countries.get)

def main():
    return compute_best_contry()

print(main())
