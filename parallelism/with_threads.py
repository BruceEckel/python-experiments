# parallelism/with_threads.py
from concurrent.futures import ThreadPoolExecutor
from scenario_tester import scenario
from cpu_intensive import cpu_intensive

if __name__ == "__main__":
    with scenario() as scenario:
        with ThreadPoolExecutor() as executor:
            scenario.results = executor.map(
                cpu_intensive, scenario.args1, scenario.args2
            )
