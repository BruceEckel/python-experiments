from multiprocessing import Pool
import time

def f(x):
    return x*x*x

if __name__ == '__main__':
    SIZE = 25
    with Pool() as pool:
        print(pool.map(f, range(SIZE)))

        for result in pool.imap_unordered(f, range(SIZE)):
            print(result)

        map_result = pool.starmap_async(f, range(SIZE))
        print(f"{map_result = }")
        print(f"{map_result.ready() = }")
        print(f"{map_result.wait() = }")
        print(f"{map_result.ready() = }")
        # print(f"{map_result.get() = }")
        print(f"{map_result.successful() = }")
