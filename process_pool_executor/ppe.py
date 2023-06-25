# https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor
import concurrent.futures
import math
import random


def num_gen(quantity: int, bits: int):
    for _ in range(quantity):
        yield random.getrandbits(bits)


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    candidates = list(num_gen(100, 60))
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for number, prime in zip(candidates, executor.map(is_prime, candidates)):
            print(f"{number} is prime: {prime}")
