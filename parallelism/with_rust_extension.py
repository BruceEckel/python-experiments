from scenario_tester import scenario
from concurrent.futures import ProcessPoolExecutor
import rust_extension

if __name__ == "__main__":
    with scenario() as scenario:
        with ProcessPoolExecutor() as executor:
            scenario.results = executor.map(
                rust_extension.cpu_intensive,
                scenario.args1,
                scenario.args2,
            )
