INPUT_FILE = '04-input3.txt'
OUTPUT_FILE = "04-result.txt"
RUNNERS_PER_TEAM = 4

class Runner:
    def __init__(self, number, time_s):
        self.number = number
        self.time = float(time_s)

    def to_string(self):
        return f"Runner(number={self.number}, time={self.time})"

class Team:
    def __init__(self, runners):
        self.runners = runners
        self.total = 0

    def add_runner(self, runner):
        if len(self.runners) == RUNNERS_PER_TEAM:
            raise Exception("Cannot add runners anymore")
        self.runners.append(runner)
        if len(self.runners) == RUNNERS_PER_TEAM:
            self.total = self.compute_total_time()

    def compute_total_time(self):
        self.runners.sort(key=lambda r: r.time)
        total = 0
        for i in range(len(self.runners)):
            total += self.runners[i].time
            if i > 0:
                passage = (self.runners[i].time - self.runners[i-1].time) ** 2
                passage = float('%.2f' % passage)
                total += passage
        return total

    def to_string(self):
        if len(self.runners) == 0:
            runners = "[]"
        else:
            runners = "[" + self.runners[0].to_string()
            for runner in self.runners[1:]:
                runners += ","
                runners += runner.to_string()
            runners += "]"
        return f"Team(runners={runners})"

def compute_score(best_team, worst_team):
    return worst_team.total - best_team.total

def get_team_compositions(teams):
    s = ""
    for team in teams:
        for runner in team.runners:
            s += runner.number
            s += " "
    return s

def write_result_to_file(result):
    with open(OUTPUT_FILE, 'w') as f:
        f.write(result)
        f.close()

def compute():
    runners = []
    with open(INPUT_FILE, 'r') as f:
        lines = f.readlines()
        number_of_teams = int(len(lines)/RUNNERS_PER_TEAM)
        for line in lines:
            runner_number, runner_time_s = line.split(",")
            runner = Runner(runner_number, runner_time_s)
            runners.append(runner)
    runners.sort(key=lambda r: r.time)
    teams = [Team([]) for t in range(number_of_teams)]
    for i in range(len(runners)):
        team_number = i%number_of_teams
        teams[team_number].add_runner(runners[i])
    teams.sort(key=lambda t: t.total)
    print(f"Computed score: {compute_score(teams[0], teams[-1])}")
    return write_result_to_file(get_team_compositions(teams))

def main():
    return compute()

main()
