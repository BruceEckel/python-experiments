from concurrent.futures import ProcessPoolExecutor
from scenario_tester import scenario
from rust_extension import cpu_intensive

if __name__ == "__main__":
    with scenario() as scenario:
        with ProcessPoolExecutor() as executor:
            scenario.results = executor.map(
                cpu_intensive, scenario.args1, scenario.args2
            )
