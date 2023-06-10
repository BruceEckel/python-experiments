from concurrent.futures import ProcessPoolExecutor
import math


def computation(n):  # CPU-intensive
    result = 0
    for i in range(10**7 * 2):
        result += math.sqrt(i**3 + i**2 + i * n)
    return result


if __name__ == "__main__":
    with ProcessPoolExecutor() as executor:
        logical_processors = executor._max_workers
        print(f"{logical_processors = }")
        results = executor.map(computation, range(logical_processors - 1))
    print(list(results))
