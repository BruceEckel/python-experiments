from concurrent.futures import ThreadPoolExecutor
from cpu_intensive import cpu_intensive
from scenario_tester import scenario

if __name__ == "__main__":
    with scenario() as scenario:
        with ThreadPoolExecutor() as executor:
            scenario.results = executor.map(
                cpu_intensive, scenario.args1, scenario.args2
            )
