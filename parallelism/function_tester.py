from concurrent.futures import ProcessPoolExecutor
from scenario_tester import scenario
from cpu_intensive import cpu_intensive


def test_cpu_intensive(ExecutorClass):
    with scenario() as s:
        with ExecutorClass() as executor:
            s.results = executor.map(cpu_intensive, s.args1, s.args2)


if __name__ == "__main__":
    test_cpu_intensive(ProcessPoolExecutor)
