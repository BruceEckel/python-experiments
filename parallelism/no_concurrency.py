from cpu_intensive import cpu_intensive
from scenario_tester import scenario

if __name__ == "__main__":
    with scenario() as scenario:
        scenario.results = [
            cpu_intensive(n, scenario.multiplier) for n in scenario.args1
        ]
